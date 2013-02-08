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
