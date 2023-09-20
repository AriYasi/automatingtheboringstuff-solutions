import random, inputupgraded

QUESTIONS = 10
correct_questions = 0

for question in range(QUESTIONS):
    n1 = random.randint(0, 10)
    n2 = random.randint(0, 10)
    calculation = n1 * n2

    prompt = f'#{question + 1}: {n1} x {n2} = '
    try:
        test = inputupgraded.input_str(prompt, retry_amount=3, allowed_regexes=[f'^{calculation}*$'], timeout=5)
    except inputupgraded.TimeoutException:
        print('Maximum time reached for this question.')
    except inputupgraded.RetryLimitException:
        print('Out of tries for this question.')
    else:
        correct_questions += 1

print(f'You got {correct_questions}/{QUESTIONS} right. That\'s %{(correct_questions/QUESTIONS) * 100:.1f}.')

