
file=open("C:/Users/HP/22112321_Mahak_BEA372/Lab 1/bank.csv",'r')
header=file.readline()
data=file.readlines()
print(header.replace('"',''))

def marital(data):
    married=0
    single=0

    for item in data:
        count=item.split(";")
        marital=count[2].strip('"')
        if marital=="married":
            married+=1
        else:
            single+=1
    print(married)
    print(single)
martial()


def prepare_age_histogram(data):
    # Prepare a histogram for age
    ages = []
    for line in data[1:]:
        customer = line.strip().split(';')
        age = int(customer[0])  # Assuming age column is at index 3
        ages.append(age)

    # Divide ages into classes of interval 10
    age_classes = {}
    for age in ages:
        age_class = age // 10 * 10
        if age_class in age_classes:
            age_classes[age_class] += 1
        else:
            age_classes[age_class] = 1

    print("Histogram for age:")
    for age_class, count in age_classes.items():
        print(f"{age_class}-{age_class + 9}: {'|' * count}")