#@markdown If, Elif, dan Else
s1, s2, s3 = map(len, input().split()))

if s1>s2<s3 or s1<s2>s3:
    print("Yeehaaw")
elif s1>s2>s3 or s1<s2<s3:
    print("Woohoohoo")
else:
    print("Hebwueh")
