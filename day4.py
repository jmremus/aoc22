import sys
# --- Day 4: Camp Cleanup ---
# Some of the pairs have noticed that one of their assignments fully contains the other. 
# For example, 2-8 fully contains 3-7, and 6-6 is fully contained by 4-6. 
# In pairs where one assignment fully contains the other, one Elf in the pair would be exclusively cleaning 
# sections their partner will already be cleaning, so these seem like the most in need of reconsideration. 
# In this example, there are 2 such pairs.
def get_input():
    pairs = []

    if len(sys.argv) < 2:
        print("ERROR: Please provide a filename as input.")
        sys.exit(1)

    with open(sys.argv[1]) as f:
        for x in f.readlines():
            pairs.append(x.strip().split(','))

    #print("Pairs are:", pairs)
    return pairs

# let's convert inputs like '2-7' to 01111110 aka bcd
def binify(s):
    a = s.split('-')
    out = 0

    #print("A is:",a)
    for x in range(int(a[0]),int(a[1])+1):
        out += 2**x
    #print("Out is:", out)

    return out  

def main():
    pairs = get_input()

    dups = 0

    for p in pairs:
        a=binify(p[0])
        b=binify(p[1])

        #print("P,a,b",p,a,b)
        if a & b == b and b <= a:
            dups += 1
        elif a & b == a and a <= b:
            dups +=1

    print("Dups are:", dups)

if __name__ == "__main__":
    main()