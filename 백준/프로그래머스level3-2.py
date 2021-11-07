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
	logs = sorted(logs)
	starts = []
	ends = []
	for log in logs:
		tmp = log.split('-')
		starts.append(time_to_num(tmp[0]))
		ends.append(time_to_num(tmp[1]))
	adv = time_to_num(adv_time)
	play = time_to_num(play_time)

	adv_start = 0
	adv_max_time = 0
	result = []
	while adv_start <= play - adv:
		adv_play_time = 0
		adv_end = adv_start + adv
		for i in range(len(starts)):
			if adv_start <= starts[i] and starts[i] <= adv_end:
				if adv_end >= ends[i]:
					adv_play_time += (ends[i] - starts[i])
				else:
					adv_play_time += (adv_end - starts[i])
			elif adv_start <= ends[i] and ends[i] <= adv_end:
				adv_play_time += (ends[i] - adv_start)
			elif starts[i] <= adv_start and ends[i] >= adv_end:
				adv_play_time += adv
		if adv_max_time < adv_play_time:
			adv_max_time = adv_play_time
			result = [adv_start]
		elif adv_max_time == adv_play_time:
			result.append(adv_start)
		adv_start += 1

	print(num_to_time(result[0]))
solution("99:59:59", "00:14:15", ["01:20:15-01:45:14", "00:40:31-01:00:00", "00:25:50-00:48:29", "01:30:59-01:53:29", "01:37:44-02:02:30"])
