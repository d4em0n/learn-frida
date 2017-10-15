import frida
import sys

if len(sys.argv) < 2:
    exit()

session = frida.attach("prog")
script = session.create_script("""
    var func = ptr("%s");
    var putsPtr = Module.findExportByName(null, 'puts');
    var puts = new NativeFunction(putsPtr, 'void', ['pointer']);
    Interceptor.replace(func, new NativeCallback( function(){
        pstr = Memory.allocUtf8String("Hijacked!!");
        puts(pstr);
        return;
    }, 'void',['void']));
""" % (sys.argv[1]))

def on_msg(msg,data):
    print msg,data

script.on('message',on_msg)
script.load()
sys.stdin.read()
