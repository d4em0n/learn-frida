import frida
import sys

session = frida.attach("read_file")
script = session.create_script("""
    Interceptor.attach(Module.findExportByName(null,"fopen"),{
        onEnter: function (args) {
            fake_data = Memory.allocUtf8String("fake_data");
            args[0] = fake_data;
            var path = Memory.readUtf8String(args[0]);
            console.log("fopen("+path+")");
        },
    });
""")
def on_message(msg,data):
    print msg

script.on('message', on_message)
script.load()
sys.stdin.read()
