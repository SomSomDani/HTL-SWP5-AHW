import requests

def sendRequest(username, voteScissors, voteRock, votePaper, voteSpock, voteLizard, apiIP = "http://127.0.0.1:5000"):
    reqUrl = apiIP + "/v1/updateRecord"
    reqUrl += "?username=" + str(username) + "&voteScissors=" + str(voteScissors)
    reqUrl += "&voteRock=" + str(voteRock) + "&votePaper=" + str(votePaper)
    reqUrl += "&voteSpock=" + str(voteSpock) + "&voteLizard=" + str(voteLizard)
    responseCode = 0
    try:
        response = requests.post(reqUrl, None)
        responseCode = response.status_code
    except:
        return 0
    return responseCode


if __name__ == "__main__":
    print("sending test request")
    code = sendRequest("testUsername", 1, 2, 3, 4, 5)
    print("Done")
    print("code=" + str(code))
