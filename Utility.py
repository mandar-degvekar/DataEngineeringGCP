class util:
    def splitandlist(input):
        l = []
        for i in input:
            try:

                l.append(int(i))

            except:
                print(i + " is not a number")

        return l