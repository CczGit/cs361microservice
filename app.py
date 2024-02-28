from flask import Flask, request, jsonify
from datetime import datetime, timedelta
import pytz
from sunrise_calc import calc_sunrise_sunset

app = Flask(__name__)


@app.route('/sunrise-sunset', methods=['GET'])
def get_sunrise_sunset():
    # convert the lat and long arguments to float
    lat = float(request.args.get('lat'))
    lng = float(request.args.get('lng'))
    # Default to UTC if no timezone is provided
    timezone_str = request.args.get('timezone', 'UTC')
    # use pytz to parse timezone
    tz = pytz.timezone(timezone_str)
    # identify date range
    date_start = request.args.get('date_start')
    date_end = request.args.get('date_end')
    # set date format YYYY-MM-DD
    date_format = "%Y-%m-%d"
    # convert dates to datetime
    start_date = datetime.strptime(date_start, date_format)
    end_date = datetime.strptime(date_end, date_format)
    # results aray initialization
    results = []

    # iterate through dates, generating the results
    while start_date <= end_date:
        # calculate sunrise/sunset time
        sunrise_ts, sunset_ts, _ = calc_sunrise_sunset(start_date.timestamp(), lat, lng)
        # modify to requested format
        sunrise_dt = datetime.fromtimestamp(sunrise_ts, pytz.utc).astimezone(tz).strftime('%I:%M:%S %p')
        sunset_dt = datetime.fromtiestamp(sunset_ts, pytz.utc).astimezone(tz).strftime('%I:%M:%S %p')
        # add to results array
        results.append({
            'date': start_date.strftime(date_format),
            'sunrise': sunrise_dt,
            'sunset': sunset_dt
        })
        # step forward one day
        start_date += timedelta(days=1)

    return jsonify(results)


if __name__ == '__main__':
    app.run(debug=True)
