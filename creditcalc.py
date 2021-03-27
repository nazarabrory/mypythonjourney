import argparse
import math
import sys

parser = argparse.ArgumentParser(description="===== Welcome to Credit Calculator =====")
parser.add_argument("--type", choices=["diff", "annuity"], help="Choose calculator type.")
parser.add_argument("-pr", "--principal", type=float, help="Input credit principal.")
parser.add_argument("-pe", "--periods", type=float, help="Input credit periods.")
parser.add_argument("-in", "--interest", type=float, help="Input credit interest.")
parser.add_argument("-pa", "--payment", type=float, help="Input credit payment")
args = parser.parse_args()
# print(len(sys.argv))
if len(sys.argv) != 5:

    print("Incorrect parameters.")
    sys.exit()
elif args.interest is None:
    print("Incorrect parameters.")
elif args.type == "diff" and args.payment is not None:
    print("Incorrect parameters.")
elif args.periods is not None and args.periods < 0:
    print("Incorrect parameters.")
else:

    class Diff:
        def __init__(self, principal, interest, periods, payments):
            self.principal = principal
            self.interest = interest
            self.periods = periods
            self.payment = payments

        def differentiated_payment(self):
            m = 1
            payment_accumulation = 0
            while m != self.periods + 1:
                dm = math.ceil(((self.principal / self.periods) + self.interest_rate() * (
                        self.principal - ((self.principal * (m - 1)) / self.periods))))
                print(f"Month {m}: paid out {dm}")
                m = m + 1
                payment_accumulation = payment_accumulation + dm
            print()
            print(f"Overpayment = {math.ceil(payment_accumulation - self.principal)}")

        def interest_rate(self):
            i = self.interest / (12 * 100)
            return i


    class Annuity:
        def __init__(self, principal, interest, periods, payments):
            self.principal = principal
            self.interest = interest
            self.periods = periods
            self.payment = payments

        def get_info(self):
            print(f"""You have just input: 
principal = {self.principal}, 
interest  = {self.interest}, 
periods   = {self.periods}, 
payment   = {self.payment}.""")

        def annuity_payment(self):
            an = math.ceil(self.principal * (self.interest_rate() * pow((1 + self.interest_rate()), self.periods) / (
                    pow((1 + self.interest_rate()), self.periods) - 1)))
            overpayment = round((an * self.periods) - self.principal)
            print(f"Your annuity payment = {an}!")
            print(f"Overpayment = {overpayment}")

        def credit_principal(self):
            p = math.floor((self.payment / (
                    (self.interest_rate() * math.pow((1 + self.interest_rate()), self.periods)) / (
                    pow((1 + self.interest_rate()), self.periods) - 1))))
            overpayment = round(((self.payment * self.periods) - p))
            print(f"Your credit principal = {p}!")
            print(f"Overpayment = {overpayment}")

        def interest_rate(self):
            i = self.interest / (12 * 100)
            return i

        def credit_periods(self):
            months = math.ceil(math.log((self.payment / (self.payment - self.interest_rate() * self.principal)),
                                        (1 + self.interest_rate())))
            overpayment = round(((self.payment * months) - self.principal))
            years = 0
            if months < 12:
                print(f"You need {months} months to repay this credit!")
            else:
                while months >= 12:
                    months = months - 12
                    years = years + 1
                if months == 0:
                    print(f"You need {years} years to repay this credit!")
                elif months != 0:
                    print(f"You need {years} years and {months} months to repay this credit!")

            print(f"Overpayment = {overpayment}")

    credit_calc_diff = Diff(args.principal, args.interest, args.periods, args.payment)
    credit_calc_annuity = Annuity(args.principal, args.interest, args.periods, args.payment)

    if args.type == "diff" and args.payment is None:
        credit_calc_diff.differentiated_payment()
    elif args.type == "annuity" and args.payment is None:
        credit_calc_annuity.annuity_payment()
    elif args.type == "annuity" and args.principal is None:
        credit_calc_annuity.credit_principal()
    elif args.type == "annuity" and args.periods is None:
        credit_calc_annuity.credit_periods()
