# -*- coding: utf-8 -*- 
import matplotlib
matplotlib.use( "agg" )
import matplotlib.pyplot as plt
import pylab


t11 = [1, 2, 3, 4, 5, 6, 7]
t12 = [1, 2, 4, 8, 16, 32, 64]

## AV-WMS (farbig)
#filename = "avwms_bench"
#title = "AV-WMS (farbig)"
#direkt = [5.5, 10.9, 12.8, 21.4, 22.8, 29.9, 31.5]
#embedded = [5.3, 10.4, 15.4, 19.8, 21.6, 30.4, 31.9]
#wms = [4.0, 5.7, 8.6, 9.7, 5.8, 1.9, pylab.nan]

## Plan fuer das Grundbuch
#filename = "grundbuchplan_bench"
#title = "Grundbuchplan"
#direkt = [2.7, 6.1, 12.3, 20.0, 31.1, 32.0, 32.0]
#embedded = [6.2, 11.9, 17.7, 25.0, 30.1, 22.7, 32.9]
#wms = [4.8, 7.3, 8.7, 12.8, 8.1, 1.6, pylab.nan]

## Basisplan
#filename = "basisplan_bench"
#title = "Basisplan"
#direkt = [3.2, 6.1, 9.3, 13.0, 14.2, 15.2, 15.7]
#embedded = [3.2, 5.7, 9.5, 13.8, 14.0, 14.9, 15.2]
#wms = [2.4, 3.6, 5.9, 6.3, 3.2, pylab.nan, pylab.nan]

## Orthofoto
#filename = "orthofoto_bench"
#title = "Orthofoto"
#direkt = [2.9, 5.6, 9.3, 14.0, 13.1, 14.6, 15.0]
#embedded = [3.3, 5.3, 9.4, 14.0, 14.0, 14.6, 14.9]
#wms = [1.8, 3.0, 4.6, 5.2, 2.6, pylab.nan, pylab.nan]

# AVWMS (req/s)
filename = "avwms_req_per_sec"
title = "AVWMS (BoFlaeche, GB-Nr. Liegenschaften)"
mapserver = [9.1, 19.2, 32.3, 35.0, 34.7,34.7, 34.7]
mapserver_fcgi = [19.4, 38.1, 62.2, 67.2, 65.9, 67.2, 67.2]
qgisserver = [12.4, 25.0, 42.7, 46.9, 46.0, 46.6, 46.8]

# AVWMS (max response time)
#filename = "avwms_max_resp_time"
#title = "AVWMS (BoFlaeche, GB-Nr. Liegenschaften)"
#mapserver = [0.6, 0.7, 0.8, 1.4, 2.9, 5.9, 11.6]
#mapserver_fcgi = [0.6, 1.2, 1.1, 1.3, 18.1, 30.2, 42.2]
#qgisserver = [0.9, 1.6, 1.7, 2.6, 25.1, 49.2, 64.5]

# Orthofoto (nearest neighbour)
#filename = "ortho_req_per_sec"
#title = "Orthofoto (nearest neighbour)"
#mapserver = [19.0, 37.5, 63.9, 66.1, 65.0, 64.6, 64.2]
#mapserver_fcgi = [32.4, 64.6, 105.4, 117.9, 116.9, 118.6, 116.6]
#qgisserver = [11.1, 21.5, 38.6, 39.3, 39.4, 39.3, 39.0]

# Orthofoto (nearest neighbour/ max_resp_time)
#filename = "ortho_max_resp_time"
#title = "Orthofoto (nearest neighbour)"
#mapserver = [0.2, 0.2, 0.2, 0.4, 1.1, 2.0, 4.2]
#mapserver_fcgi = [0.1, 1.1, 1.1, 1.1, 5.1, 11.1, 18.1]
#qgisserver = [0.2, 1.4, 1.5, 2.1, 19.3, 23.2, 64.1]

# Orthofoto (average)
#filename = "ortho_resampling_req_per_sec"
#title = "Orthofoto (average)"
#mapserver = [4.4, 8.3, 14.9, 16.1, 15.9, 16.0, 16.0]
#mapserver_fcgi = [4.9, 9.7, 17.4, 18.1, 17.9, 18.2, 18.4]
#qgisserver = [6.3, 12.4, 22.3, 23.2, 23.1, 23.0, 23.2]

# Orthofoto (average / max_resp_time)
#filename = "ortho_resampling_max_resp_time"
#title = "Orthofoto (average)"
#mapserver = [4.8, 4.8, 5.2, 10.5, 20.9, 42.1, 84.5]
#mapserver_fcgi = [4.6, 4.7, 5.0, 10.0, 58.5, 64.1, 65.8]
#qgisserver = [0.8, 1.4, 1.6, 2.8, 25.3, 47.1, 64.1]

plt.plot(t11, mapserver,  marker='s', color='b', label='MapServer (CGI)', linewidth='2')
plt.plot(t11, mapserver_fcgi, marker='^', color='m', label='MapServer (FCGI)', linewidth='2')
plt.plot(t11, qgisserver, marker='o', color='y', label='QGIS-Server', linewidth='2')

plt.xlabel('N Requests')
plt.ylabel('Throughput (Req/s)')
#plt.ylabel('Max response time (s)')
plt.title(title)
plt.legend(bbox_to_anchor=(0.02, 0.98), loc=2, borderaxespad=0.)

plt.xticks( [1, 2, 3, 4, 5, 6, 7],  t12 )
plt.ylim([0, 70])
#plt.ylim([0, 50])

plt.grid(b=True, which='major', linestyle='dotted') 

plt.savefig('./'+filename+'.png', dpi=100)
