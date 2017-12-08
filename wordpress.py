import urllib2,re,os,time,sys,random
def banner():
    clear = "\x1b[0m"
    colors = [36, 32, 34, 35, 31, 37]
    x = """          \\||
         ,'_,-\             C  O  D  E  D    B  Y    N O V A
         ;'____\

         || =\=|
         ||  - |
     ,---'._--''-,,---------.--.----_,  ###### Wordpress Version detector ######
    / `-._- _--/,,|  ___,,--'--'._<
   /-._,  `-.__;,,|'
  /   ;\      / , ;
 /  ,' | _ - ',/, ;
(  (   |     /, ,,;

         """
    for N, line in enumerate(x.split("\n")):
        sys.stdout.write("\x1b[1;%dm%s%s\n" % (random.choice(colors), line, clear))
        time.sleep(0.05)
def cls():
    linux = 'clear'
    windows = 'cls'
    os.system([linux, windows][os.name == 'nt'])
a = sys.argv[1]
cls()
banner()
b = urllib2.urlopen(a).read()
pattern = re.compile(r'<meta name="generator" content="WordPress (.*)" />', re.M)
print 'WordPress version Is {}'.format(re.findall(pattern, b))
raw_input()
cls()

