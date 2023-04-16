test_design_writers = [1, 3, 5]
scripters = [2, 3, 4, 6, 7, 8]
reviewers = [1, 2, 3, 9, 10]
out_of_office_today = [2, 5, 6, 1]

all_testers = sorted(set(test_design_writers + scripters + reviewers + out_of_office_today))

script_writers_only = sorted(set(scripters) - set(test_design_writers) - set(reviewers))

working_today = sorted(set(all_testers) - set(out_of_office_today))

script_reviewers_working_today = sorted(set(scripters) & set(reviewers) & set(working_today))

print("Все тестировщики в команде:")
print(all_testers)

print("Тестировщики, которые могут только писать скрипты:")
print(script_writers_only)

print("Тестировщики, которые сегодня на работе:")
print(working_today)

print("Тестировщики, которые могут писать и ревьюить скрипты, и которые сегодня на работе:")
print(script_reviewers_working_today)
