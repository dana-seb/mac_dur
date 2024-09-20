# Function that computes MacaulayDuration given imputes

print('\n')


cf = [3.7, 4.9, 107]
full = 95
r = .06
frac_coupon = 0


def mac_dur(cf, full, r, frac_coupon):
    macaulay_dur = []
    for i in range(len(cf)):
        n = (i+1)
        duration = (n - frac_coupon)*(cf[i]/(1+r)**(n - frac_coupon))/full
        macaulay_dur.append(duration)
    return round(sum(macaulay_dur),3)


print(mac_dur(cf, full, r, frac_coupon))

print('\n')