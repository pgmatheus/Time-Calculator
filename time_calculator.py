def add_time(start, duration, day = ''):
  string = start.replace(':',' ').split(' ')
  dur = duration.split(':')
  totaltim = int(string[0])*60+int(string[1])+int(dur[0])*60+int(dur[1])
  if (string[2] == 'PM'):
    totaltim = totaltim+60*12
  nhour = totaltim//60
  ndays = nhour//24
  hc =  int(nhour%24)
  nmin = totaltim%60
  if (hc > 11):
    hc = hc-12
    if (hc == 0):
      hc = 12
    ampm = 'PM'
  else:
    if (hc == 0):
      hc = 12
    ampm = 'AM'
  if (nmin < 10):
    nmin = '0' + str(nmin)
  fin = str(hc) + ':' + str(nmin) + ' ' + str(ampm)
  if (day != ""):
    vday = switch(day.lower())
    if (ndays>0 and ndays != 1):
      if ndays > 6:
        dday = switch2((ndays%7+vday)%7)
      else:
        if (ndays+vday > 7):
          dday = switch2((ndays+vday)%7)
        else:
          dday = switch2(ndays+vday)
      fin = fin + ', ' + dday + ' (' + str(ndays) + " days later)"
    elif ndays == 1:
      fin = fin + ', '+ switch2(vday+1) + ' (next day)'         
    else:
      fin = fin + ', ' + day
  elif (ndays == 1):
    fin = fin + ' (next day)'
  elif (ndays > 1):
    fin = fin + " (" + str(ndays) + ' days later)'
  return fin

def switch(day):
  sw = {
    'monday':1,
    'tuesday':2,
    'wednesday':3,
    'thursday':4,
    'friday':5,
    'saturday':6,
    'sunday':7
  }
  return sw.get(day)

def switch2(day):
  sw = {
    1:'Monday',
    2:'Tuesday',
    3:'Wednesday', 
    4:'Thursday',
    5:'Friday',
    6:'Saturday',
    7:'Sunday'
  }
  return sw.get(day)


