# Initialize all men and women to free
N=4

# This function returns true if 
# woman 'w' prefers man 'm1' over man 'm'
def wPrefersM1OverM(prefer, w, m, m1):
    for i in range(N):
        # If m1 comes before m in list of w, 
        # then w prefers her current engagement,
        # don't do anything, else free her current
        # engagement and engage her with m
        if(prefer[m][i]==m1):
            return True
        if(prefer[w][i]==m):
            return False

def stableMarriage(prefer):
    # Stores partner of women. This is our output 
    # array that stores passing information. 
    # The value of wPartner[i] indicates the partner 
    # assigned to woman N+i. Note that the woman numbers 
    # between N and 2*N-1. The value -1 indicates 
    # that (N+i)'th woman is free
    wPartner=[-1 for i in range(N)]

    mFree=[False for i in range(N)]

    freeCount=N

    # while there are free men
    while(freeCount>0):
        #pick first free man
        m=0
        while(m<N):
            if(mFree[m]==False):
                break
            m += 1

        # One by one go to all women according to 
        # m's preferences. Here m is the picked free man
        i=0
        while i<N and mFree[m]==False:
            w=prefer[m][i]

            # The woman of preference is free, 
            # w and m become partners
            if(wPartner[w-N]==-1):
                wPartner[w-N]=m
                mFree[m]=True
                freeCount -= 1
            else:
                # If w is not free
                # Find current engagement of w
                m1=wPartner[w-N]
                # If w prefers m over her current engagement m1,
                # then break the engagement between w and m1 and
                # engage m with w.
                if(wPrefersM1OverM(prefer, w, m, m1) == False):
                    wPartner[w-N]=m
                    mFree[m]=True
                    mFree[m1]=False
            
            i += 1
    
    print("Woman ", " Man")
    for i in range(N):
        print(i + N, "\t", wPartner[i])


prefer = [[7, 5, 6, 4], [5, 4, 6, 7],
          [4, 5, 6, 7], [4, 5, 6, 7],
          [0, 1, 2, 3], [0, 1, 2, 3],
          [0, 1, 2, 3], [0, 1, 2, 3]]
  
stableMarriage(prefer)