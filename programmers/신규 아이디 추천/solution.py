import re

def solution(new_id):
    st = new_id
    st = st.lower()
    st = re.sub("[^a-z0-9\-_.]", "", st)
    st = re.sub("\.+", ".", st)
    st = st.strip(".")
    st = "a" if len(st) == 0 else st[:15]
    st = st.rstrip(".")
    print(st[-1])
    st = st + "".join(st[-1] for x in range(3- len(st))) if len(st) <= 2 else st

    answer = st
    return answer

if __name__ == '__main__':
    new_id = "...!@BaT#*..y.abcdefghijklm"
    
    result = solution(new_id)
    print(result)