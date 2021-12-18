
def deeper(report):
    """
    takes a list of depth measurements and determines how many times the depth increases

    Inputs:
        report (list of strings): list of depth measurements 

    Returns: number of times depth increases
    """
    previous = 100000000.0
    deeper = 0
    for measurement in report:
        measurement = int(measurement)
        if previous < measurement:
            deeper = deeper + 1
        previous = measurement
    return deeper

    print(deeper)