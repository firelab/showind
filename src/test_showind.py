#!/usr/bin/env python
###############################################################################
# $Id$
#
#  Project:  showind
#  Purpose:  Display and subset wind data
#  Author:   Kyle Shannon <kyle@pobox.com>
#
###############################################################################
#  Copyright (c) 2013, Kyle Shannon <kyle@pobox.com>
#
#  Permission is hereby granted, free of charge, to any person obtaining a
#  copy of this software and associated documentation files (the "Software"),
#  to deal in the Software without restriction, including without limitation
#  the rights to use, copy, modify, merge, publish, distribute, sublicense,
#  and/or sell copies of the Software, and to permit persons to whom the
#  Software is furnished to do so, subject to the following conditions:
#
#  The above copyright notice and this permission notice shall be included
#  in all copies or substantial portions of the Software.
#
#  THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS
#  OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
#  FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL
#  THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
#  LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING
#  FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER
#  DEALINGS IN THE SOFTWARE.
###############################################################################

#import bigbutte

#example to fetch a single point and create a kml
#p = bigbutte.mean_flow_point('R26', '2010-09-04T16:00:00', '2010-09-04T17:00:00', True)
#p.create_kml()

#fetch a field
#import bigbutte
#plot = 'R6'
#start_time = '2010-08-01T12:00:00'
#end_time = '2010-08-02T14:00:00'
#ignore_crappy = True

#point = bigbutte.mean_flow_point(plot, start_time, end_time, ignore_crappy)
#point.create_kmz('point.kmz')
#point.create_csv('point.csv')



#field = bigbutte.mean_flow_field(start_time, end_time, True)
#field.create_kmz('test.kmz', True)
#field.create_csv('out.csv', True)
#fetch an inl forecast
#fc = bigbutte.inl_fcast('')

import showind
plot = 'S5-81'
start = '2012-11-01T19:30:00'
end = '2012-11-01T21:30:00'

sw = showind.ShoWind('dan.sqlite', start, end)
sw.create_field_kmz('test.kmz')
