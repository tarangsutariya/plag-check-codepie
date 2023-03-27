import mosspy
import os
userid = 384569079

dirs = os.listdir("submission")
print(dirs)
    



for language in dirs:
    print("for %s"%(language))
    m = mosspy.Moss(userid, language)
    if language == "python":
        extens = ".py"
    elif language == "cpp":
        extens = ".cpp"
    elif language == "java":
        extens = ".java"


    # Submission Files
    prbs = os.listdir(os.path.join("submission",language))
    for prb_id in prbs:
        m.addFilesByWildcard("submission/%s/%s/*"%(language,prb_id)+extens)

        # progress function optional, run on every file uploaded
        # result is submission URL
        url = m.send(lambda file_path, display_name: print('*', end='', flush=True))
        print()
        
        print ("%s Report Url: "%(prb_id) + url)