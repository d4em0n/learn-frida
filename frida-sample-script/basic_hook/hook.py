import frida
import sys

if len(sys.argv) < 3:
    print "Use : %s <program> <func addr>" % (sys.argv[0])
    exit()

session = frida.attach(sys.argv[1])
script = session.create_script("""
    Interceptor.attach(ptr("%s"), {
        onEnter: function(args){
            console.log("Arg : "+args[0].toInt32());
        }
    });
""" % (int(sys.argv[2], 16)))
script.load()
sys.stdin.read()

