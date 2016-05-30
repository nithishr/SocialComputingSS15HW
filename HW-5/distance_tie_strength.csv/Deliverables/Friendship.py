import csv
import operator
import igraph
import pylab

def printInterval(ties, start_dist, end_dist):
    """Print the details of the interval in between the interval specified among the ties"""
    for tie in ties:
        if int(tie['start_dist'])==start_dist and int(tie['end_dist'])==end_dist:
            print str(tie['start_dist'])+'-'+str(tie['end_dist'])+' : '+str(tie['prob']) + ' : '+str(tie['ties'])
            # print 'No. of ties: ',str(tie['ties'])

tie_detail = []
#Read the CSV file containing the tie strengths & distances.
with open('distance_tie_strength_list_clean.csv','r') as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
        tie_detail.append(list(map(float,row)))

# print tie_detail[0]
# distances = [ tie for tie in tie_detail ]
# distances.sort()

#Sort the tie strengths by distance
tie_detail.sort(key=operator.itemgetter(0))
# print tie_detail[0],tie_detail[-1],distances[0],distances[-1]
# for count in xrange(len(tie_detail)):
#     if tie_detail[count][0]!=distances[count][0] or tie_detail[count][1]!=distances[count][1]:
#         print tie_detail[count],distances[count]

#Set friendship threshold to 50
friendship_thresh = 50
for tie in tie_detail:
    if tie[1]>=friendship_thresh:
        tie.append(True)
    else:
        tie.append(False)

#Check friendship assignment
# for tie in tie_detail:
#     if tie[2]==True and tie[1]<friendship_thresh:
#         print tie

# print tie_detail[0:10],tie_detail[-10:0]
# print len(tie_detail)

#Perform the tie analysis by dividing the relationships into buckets of distance 50Km
tie_analysis = []
cur_dist = 0.0
dist_incr = 50
tie_index = 0
while cur_dist <= tie_detail[-1][0]:
    group_stats = {'friendships':0.0,'ties':0.0}
    while cur_dist <= tie_detail[tie_index][0] and tie_detail[tie_index][0] < cur_dist+dist_incr:
        group_stats['ties'] += 1
        if tie_detail[tie_index][2]==True:
            group_stats['friendships'] += 1
        tie_index += 1
        if tie_index == len(tie_detail):
            break
    if group_stats['ties']!=0:
        group_stats['prob']=group_stats['friendships']/group_stats['ties']
    else:
        group_stats['prob']=0.0
    # print tie_index
    group_stats['start_dist'] = cur_dist
    group_stats['end_dist'] = cur_dist + dist_incr
    tie_analysis.append(group_stats)
    cur_dist += dist_incr

# print tie_analysis[0:5]
# print tie_analysis[-1:-6:-1]
#Check the counts
# count = 0
# for tie in tie_analysis:
#     count += tie['ties']
# print count, len(tie_analysis)

#Check histogram to verify the intervals
# distances_list = [i[0] for i in tie_detail ]
# hist = igraph.Histogram(bin_width=100,data=distances_list)
# print hist
# print hist.n

#Print the entire interval
# for tie in tie_analysis:
#     print str(tie['start_dist'])+'-'+str(tie['end_dist'])+' : '+str(tie['prob'])

#Plotting the variation in probablities with the distances
pylab.figure()
pylab.plot(range(0,int(tie_analysis[-1]['end_dist']),dist_incr),[tie['prob'] for tie in tie_analysis])
pylab.show()

#Print the interval details
# printInterval(tie_analysis,0,50)
# printInterval(tie_analysis,50,100)
# printInterval(tie_analysis,150,200)
# printInterval(tie_analysis,250,300)
# printInterval(tie_analysis,5300,5350)
# printInterval(tie_analysis,6000,6050)
# printInterval(tie_analysis,6050,6100)
# printInterval(tie_analysis,7300,7350)
# printInterval(tie_analysis,7350,7400)