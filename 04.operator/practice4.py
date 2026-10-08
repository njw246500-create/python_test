'''
성적표를 참고하여 총 이수학점과 평균학점을 구하기

파이썬(3) = A+(4.5)
운영체제(2) = B0(4.0)
AI(3) = A0(4.0)
'''

total = 3 + 2 + 3

average = ( 4.5 * 3 + 4.0 * 2 + 4.0 * 3) / total

print("총 이수학점 : %d, 평점평균 : %.2f" %(total, average))


'''
total_points = (Python*A) + (os*B0) + (ai * A0)
total_credits = python + os + AI
avg_credits = total_points / total_credits
print(f"총 이수 학점 : {total_credits}학점")
print(f"평균학점 : {avg_credits : .2f}")

'''