import statistics as s
import matplotlib.pyplot as plt
def get_results(path,bins = 100):
    f = open(path).readlines()
    to_results = []
    for res in f:
        if "Response time" in res:
            to_results.append(res)
    results =[float(x.replace("Response time ","").replace("\n","")) for x in to_results]
    print("Mean response time: {} \nMax response time: {} \nMin response time: {}".format(s.mean(results),max(results),min(results)))
    res = plt.hist(results,bins=100)
    plt.title('Response time for {} attempts during {} connection'.format(path.split(".")[-2],path.split(".")[-3]))
    plt.ylabel('Nr. of responses')
    plt.xlabel('Response time [s]')
    plt.show()
    