from Utilities.OTP import get_otp


class Otp:
    otp = get_otp.otp1()
    otp_split = [str(i) for i in str(otp[0])]
    for i in range(5):
        print(otp_split[i])