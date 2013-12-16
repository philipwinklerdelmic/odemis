# -*- coding: utf-8 -*-
'''
Created on 26 Feb 2013

@author: Éric Piel

Copyright © 2013 Éric Piel, Delmic

This file is part of Odemis.

Odemis is free software: you can redistribute it and/or modify it under the terms 
of the GNU General Public License version 2 as published by the Free Software 
Foundation.

Odemis is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; 
without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR 
PURPOSE. See the GNU General Public License for more details.

You should have received a copy of the GNU General Public License along with 
Odemis. If not, see http://www.gnu.org/licenses/.
'''
# Various helper functions that have a generic usefulness
# Warning: do not put anything that has dependencies on non default python modules

from __future__ import division

import errno
from functools import wraps
import logging
import math
from odemis import model
import os
import signal
import threading


def find_closest(val, l):
    """
    finds in a list the closest existing value from a given value
    """ 
    return min(l, key=lambda x:abs(x - val))

def index_closest(val, l):
    """
    finds in a list the index of the closest existing value from a given value
    Works also with dict and tuples.
    """
    if isinstance(l, dict):
        return min(l.items(), key=lambda x:abs(x[1] - val))[0]
    else:
        return min(enumerate(l), key=lambda x:abs(x[1] - val))[0]

def almost_equal(a, b, atol=1e-18, rtol=1e-7):
    """
    Compares two floats within a margin (to handle rounding errors).
    a (float)
    b (float)
    rtol (float): relative tolerance
    returns (bool): True if a and b are almost equal
    """
    if a == b:
        return True

    tol = max(atol, max(abs(a), abs(b)) * rtol)
    if abs(a - b) <= tol:
        return True

    return False


def rect_intersect(ra, rb):
    """
    Computes the rectangle representing the intersection area of two rectangles
    (aligned along the axes).
    ra (tuple of 4 floats): position of the first rectangle left, top, right, bottom
    rb (tuple of 4 floats): position of the second rectangle
    return (None or tuple of 4 floats): None if there is no intersection, or
     the rectangle representing the intersection 
    Note that the rectangles can have the top/bottom and left/right in any order,
    but the return value will always have top < bottom and left < right.
    """

    # Make sure that t<b and l<r
    ra = (min(ra[0], ra[2]), min(ra[1], ra[3]),
          max(ra[0], ra[2]), max(ra[1], ra[3]))

    rb = (min(rb[0], rb[2]), min(rb[1], rb[3]),
          max(rb[0], rb[2]), max(rb[1], rb[3]))

    # Any intersection?
    if ra[0] >= rb[2] or ra[2] <= rb[0] or ra[1] >= rb[3] or ra[3] <= rb[1]:
        return None

    inter = (max(ra[0], rb[0]), max(ra[1], rb[1]),
             min(ra[2], rb[2]), min(ra[3], rb[3]))

    return inter

def normalize_rect(rect):
    """
    Ensure that a rectangle has a the left less than right, and top less than
    bottom.
    rect (iterable of 4 floats): left, top, right, bottom
    return (iterable of 4 floats): left, top, right, bottom
    """
    l, t, r, b = rect
    if l > r:
        l, r = r, l
    if t > b:
        t, b = b, t

    nrect = type(rect)((l, t, r, b))
    return nrect


class TimeoutError(Exception):
    pass

# TODO: only works on Unix, needs a fallback on windows (at least, don't complain)
# from http://stackoverflow.com/questions/2281850/timeout-function-if-it-takes-too-long-to-finish
# see http://code.activestate.com/recipes/577853-timeout-decorator-with-multiprocessing/
# for other implementation
def timeout(seconds):
    """
    timeout decorator. Stops a function from executing after a given time. The
      function will raise an exception in this case.
    seconds (0 < float): time in second before the timeout
    """
    assert seconds > 0
    def decorator(func):
        def handle_timeout(signum, frame):
            raise TimeoutError("Function took more than %g s to execute" % seconds)

        def wrapper(*args, **kwargs):
            signal.signal(signal.SIGALRM, handle_timeout)
            signal.setitimer(signal.ITIMER_REAL, seconds) # same as alarm, but accepts float
            try:
                result = func(*args, **kwargs)
            finally:
                signal.setitimer(signal.ITIMER_REAL, 0)
            return result

        return wraps(func)(wrapper)

    return decorator

class RepeatingTimer(threading.Thread):
    """
    An almost endless timer thread. 
    It stops when calling cancel() or the callback disappears.
    """
    def __init__(self, period, callback, name="TimerThread"):
        """
        period (float): time in second between two calls
        callback (callable): function to call
        name (str): fancy name to give to the thread
        """
        threading.Thread.__init__(self, name=name)
        self.callback = model.WeakMethod(callback)
        self.period = period
        self.daemon = True
        self._must_stop = threading.Event()
    
    def run(self):
        # use the timeout as a timer
        try:
            while not self._must_stop.wait(self.period):
                try:
                    self.callback()
                except model.WeakRefLostError:
                    # it's gone, it's over
                    return
        except Exception:
            logging.exception("Failure while calling a repeating timer")
        finally:
            logging.debug("Repeating timer thread over")
        
    def cancel(self):
        self._must_stop.set()
