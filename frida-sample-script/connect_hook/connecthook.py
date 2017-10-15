from __future__ import print_function
import frida
import sys

"""
    Simple hooking using frida, by hooking connect function
    and print ip:port that want to connect.
    (sorry if my bad english)
    
    18 June 2017, d4em0n
    
"""
if( len(sys.argv) <= 1 ):
    print("use : python %s <processname>" % (sys.argv[0]))
    exit()

session = frida.attach(sys.argv[1])
script = session.create_script("""
    Interceptor.attach( Module.findExportByName(null,"connect") , {
        onEnter: function (args) {
            var swap16 = function (val){
                return ((val & 0xFF) << 8)
                           | ((val >> 8) & 0xFF);
            }
            var ntoa = function (val){
                var ip = "";
                ip += (val & 0xff).toString()+".";
                ip += ((val & 0xff00) >> 8).toString()+".";
                ip += ((val & 0xff0000) >> 16).toString()+".";
                ip += ((val & 0xff000000) >>> 24).toString();
                return ip;
            }
            var port = swap16(Memory.readU16(ptr(parseInt(args[1])+2)));
            var ip = ntoa(Memory.readU32(ptr(parseInt(args[1])+4)));
            send("%s connect to "+ip+":"+port);
            Memory.writeU32(ptr(parseInt(args[1])+4),16777343);
            console.log("    `--- Redirecting to 127.0.0.1:"+port);
            send("connect(" + "sockfd=" + args[0]+ ", addr=" + args[1]+ ", addrlen=" + args[2] + ")");
       }
        
    });
 """ % (sys.argv[1]))
def on_message(message, data):
    if message['type'] == 'error':
        print("[!] " + message['stack'])
    elif message['type'] == 'send':
        print("[i] " + message['payload'])
    else:
        print(message)

script.on('message', on_message)
script.load()
sys.stdin.read()
