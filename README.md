## Sunrise - Sunset API
# How to use 
 To use, run the script and then make an API call in this format: http://localhost:5000/sunrise-sunset?lat=38.907192&lng=-77.036873&date_start=1990-05-01&date_end=1990-07-01
# Parameters:
1. lat: Latitude of the location, expected format is float
2. long: Longitude of the location, expected format is float
3.  date_start: beginning date for the array
4.   date_end: ending date for the array
5.    timezone: OPTIONAL: timezone for which to configure the results
# Sample response:
[
    {
        "date": "1990-05-01",
        "sunrise": "10:11:11 AM",
        "sunset": "12:01:38 AM"
    },
    {
        "date": "1990-05-02",
        "sunrise": "10:10:01 AM",
        "sunset": "12:02:37 AM"
    },
    {
        "date": "1990-05-03",
        "sunrise": "10:08:51 AM",
        "sunset": "12:03:35 AM"
    },
    {
        "date": "1990-05-04",
        "sunrise": "10:07:43 AM",
        "sunset": "12:04:34 AM"
    },
    {
        "date": "1990-05-05",
        "sunrise": "10:06:37 AM",
        "sunset": "12:05:32 AM"
    },
    {
        "date": "1990-05-06",
        "sunrise": "10:05:31 AM",
        "sunset": "12:06:30 AM"
    },
    {
        "date": "1990-05-07",
        "sunrise": "10:04:27 AM",
        "sunset": "12:07:28 AM"
    },
    {
        "date": "1990-05-08",
        "sunrise": "10:03:25 AM",
        "sunset": "12:08:26 AM"
    },
    {
        "date": "1990-05-09",
        "sunrise": "10:02:23 AM",
        "sunset": "12:09:23 AM"
    },
    {
        "date": "1990-05-10",
        "sunrise": "10:01:23 AM",
        "sunset": "12:10:20 AM"
    },
    {
        "date": "1990-05-11",
        "sunrise": "10:00:25 AM",
        "sunset": "12:11:17 AM"
    },
    {
        "date": "1990-05-12",
        "sunrise": "09:59:28 AM",
        "sunset": "12:12:14 AM"
    },
    {
        "date": "1990-05-13",
        "sunrise": "09:58:32 AM",
        "sunset": "12:13:10 AM"
    },
    {
        "date": "1990-05-14",
        "sunrise": "09:57:38 AM",
        "sunset": "12:14:05 AM"
    },
    {
        "date": "1990-05-15",
        "sunrise": "09:56:45 AM",
        "sunset": "12:15:01 AM"
    }
]
