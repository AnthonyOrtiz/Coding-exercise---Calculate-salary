''' class pricipal '''

import dataExtraction
import financialDep


def main():
    
    dataSchedules = dataExtraction.getDataWorkers()


    financialDep.calculateSalary(dataSchedules)


if __name__ == "__main__":
    main()