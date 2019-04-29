
def logsanalysis(logs):
    filterlst = []
    for line in logs.splitlines():
        if "\"" in line:
            subline = line.split(" ")
            rline = subline[1].replace("\"", "")
            filterlst.append(rline.upper())
            filterlst.sort()
    return filterlst

if __name__ == "__main__":

    logs = '''

　
111.30.144.7 "POST /mock/login/?t=GET HTTP/1.1" 200

　

111.30.144.7 "Get /mock/users/?t=POST HTTP/1.1" 200

　

111.13.100.92 "Post /mock/login/ HTTP/1.1" 200

　

223.88.60.88 "GET /mock/users/?t=POST HTTP/1.1" 200

　

111.30.144.7 "GET /mock/users/ HTTP/1.1" 200

　

'''
    filterlst = logsanalysis(logs)
    
    print("GET: {}\nPOST: {}".format(filterlst.count("GET"), filterlst.count("POST")))




