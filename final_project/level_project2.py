import csv
from datetime import datetime, timedelta
from dateutil.relativedelta import relativedelta

# Function to calculate the installment amount
def calculate_installment_amount(total_fees, total_installments, deposit_fees):
    remainingamount = total_fees - deposit_fees
    return remainingamount / total_installments


def is_weekend(date):
    return date.weekday() in [4, 5]
def calculate_number_of_installments(payment_type, total_days):
    if payment_type == 'ANNUAL':
        return total_days // 365
    elif payment_type == 'QUARTER':
        return total_days // 90
    elif payment_type == 'MONTHLY':
        return total_days // 30
    elif payment_type == 'HALF_ANNUAL':
        return total_days // 180
    else:
        raise ValueError(f"Unsupported payment type: {payment_type}")


# Read contract data from CSV file
with open('C:\\Users\\ThinkPad\\Contracts.csv', mode='r') as csv_file:
    reader = csv.DictReader(csv_file)
    data = list(reader)


for contract in data:
    payment_type = contract['contract_payment_type']
    client_name = contract['client_name']
    contract_start_date = datetime.strptime(contract['contract_startdate'], '%d/%m/%Y')
    contract_end_date = datetime.strptime(contract['contract_enddate'], '%d/%m/%Y')
    contract_total_fees = float(contract['contract_total_fees'])




    contract_max_grace_period = int(contract['max_grace_period'])
    if contract['contract_deposit_fees']:
        contract_deposit_fees = float(contract['contract_deposit_fees'])
    else:
        contract_deposit_fees = 0
    total_days = (contract_end_date - contract_start_date).days


    total_installments = calculate_number_of_installments(payment_type, total_days)
    installment_amount = calculate_installment_amount(contract_total_fees, total_installments, contract_deposit_fees)

    # Construct the output file path starting with the contract number
    output_file_path = f'C:\\Users\\ThinkPad\\{contract["contract_id"]}_{client_name.replace(" ", "_")}_installments.csv'


    with open(output_file_path, mode='w', newline='') as csv_file:
        header = ['installment_serial', 'installment_date', 'installment_amount', 'max_grace_date']
        writer = csv.writer(csv_file)
        writer.writerow(header)


        for i in range(total_installments):


            if payment_type == 'ANNUAL':
                installment_date = contract_start_date + relativedelta(years=i)
            elif payment_type == 'QUARTER':
                installment_date = contract_start_date + relativedelta(months=i * 3)
            elif payment_type == 'MONTHLY':
                installment_date = contract_start_date + relativedelta(months=i)
            elif payment_type == 'HALF_ANNUAL':
                installment_date = contract_start_date + relativedelta(months=i * 6)



            while is_weekend(installment_date):
                installment_date += timedelta(days=1)


            grace_period_days = int(contract['max_grace_period'])
            grace_period = timedelta(days=grace_period_days)
            max_grace_date = installment_date + grace_period

            while is_weekend(max_grace_date):
                max_grace_date += timedelta(days=1)

            writer.writerow([i, installment_date.strftime('%d/%m/%Y'), installment_amount,
                             max_grace_date.strftime('%d/%m/%Y')])
