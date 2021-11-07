def time_to_num(time):
	hours, minutes, seconds = map(int, time.split(':'))
	num = hours * 60 * 60 + minutes * 60 + seconds
	return num

def num_to_time(num):
	hours = num // 3600
	num %= 3600
	minutes = num // 60
	num %= 60
	result = (("0" + str(hours)) if len(str(hours)) == 1 else str(hours)) + ":" \
		+ (("0" + str(minutes)) if len(str(minutes)) == 1 else str(minutes)) + ":"\
		+ (("0" + str(num)) if len(str(num)) == 1 else str(num))
	return result

def solution(play_time, adv_time, logs):
	play_time = time_to_num(play_time)
	adv_time = time_to_num(adv_time)
	all_times = [0 for _ in range(play_time + 1)]
	for log in logs:
		start, end = log.split('-')
		all_times[time_to_num(start)] += 1
		all_times[time_to_num(end)] -= 1

	for i in range(1, play_time + 1):
		all_times[i] = all_times[i] + all_times[i-1]

	for i in range(1, play_time + 1):
		all_times[i] = all_times[i] + all_times[i-1]

	most_view = 0
	max_time = all_times[adv_time]
	for start in range(1, play_time):
		# 광고 재생 종료 시간 >= 영상 재생 종료 시간 이면 마지막시간을 영상 재생 종료 시간으로 둔다.
		end = play_time if start + adv_time >= play_time else start + adv_time
		# 시청자 수가 이전 보다 많을 때
		if max_time < all_times[end] - all_times[start]:
			max_time = all_times[end] - all_times[start]
			# all_times[end] - all_times[start] 는 start + 1초부터 end초 사이의 누적이기 때문에 1을 더해준다.
			most_view = start + 1

	print(num_to_time(most_view))

solution("02:03:55", "00:14:15", ["01:20:15-01:45:14", "00:25:50-00:48:29", "00:40:31-01:00:00", "01:37:44-02:02:30", "01:30:59-01:53:29"])
solution("99:59:59", "25:00:00", ["69:59:59-89:59:59", "01:00:00-21:00:00", "79:59:59-99:59:59", "11:00:00-31:00:00"])
solution("50:00:00", "50:00:00", ["15:36:51-38:21:49", "10:14:18-15:36:51", "38:21:49-42:51:45"])
