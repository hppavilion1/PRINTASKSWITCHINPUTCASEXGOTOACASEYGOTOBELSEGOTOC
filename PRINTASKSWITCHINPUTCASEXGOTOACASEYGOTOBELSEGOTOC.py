import re
import sys

def isliteral(s):
    if re.match(r'[0-9]+', s) or s[0] == '"' and s[-1] == '"':
        return True
    return False

def lexline(line):
    r=[]
    s=0
    while s < len(line):
        if re.match(r'^"[^"]*"', line[s:]):
            #print('String')
            m = re.match(r'^"[^"]*"', line[s:])
            r.append(m.group(0))
            s+=len(m.group(0))
            
        elif re.match(r'^PRINT', line[s:]):
            r.append('PRINT')
            s += 5
            
        elif re.match(r'^SWITCH', line[s:]):
            r.append('SWITCH')
            s += 6
            
        elif re.match(r'^CASE', line[s:]):
            r.append('CASE')
            s += 4
            
        elif re.match(r'^ELSE', line[s:]):
            r.append('ELSE')
            s += 4
            
        elif re.match(r'^GOTO', line[s:]):
            r.append('GOTO')
            s += 4

        elif re.match(r'^ASK', line[s:]):
            r.append('ASK')
            s += 3
            
        elif re.match(r'^[A-Z]+', line[s:]):
            m = re.match(r'^[A-Z]+', line[s:])
            r.append(m.group(0))
            s += len(m.group(0))
            
        elif re.match(r'^[0-9]+', line[s:]):
            #print('Num')
            m = re.match(r'^[0-9]+', line[s:])
            r.append(m.group(0))
            s += len(m.group(0))
            
        elif re.match(r'^\s', line[s:]):
            #print('Space')
            s += 1

        else:
            raise ValueError('Invalid String '+line[s:])
        #print r
    return r

def run(script):
    script = script.split('\n')
    for line in script:
        line = lexline(line)
        i = 0
        while i < len(line):
            if line[i] == 'PRINT':
                if isliteral(line[i+1]):
                    print line[i+1].strip('"')
                else:
                    print env[line[i+1]]
                i+=1
            i+=1

if __name__ == '__main__':
    run(raw_input())
    raw_input()
