//Jason Krasavage
//Going to use some of the info on this link to figure out syncing osc messages with arguments and passing those into synthdefs etc.
//https://theseanco.github.io/howto_co34pt_liveCode/6-2-OSC-and-Data-Streams/


NetAddr.localAddr //usually returns "a NetAddr(127.0.0.1, 57120)"

n = NetAddr.new("127.0.0.1", 57120); //redundant, can use "NetAddr.localAddr" instead

o = OSCFunc({ arg msg, time, addr, recvPort; [msg, time, addr, recvPort].postln; }, '/goodbye', n);

OSCFunc.trace(true); //lets you see the OSC stream for ALL ports (so it won't filter out the /status.reply messages, after running this and running the BlockParser.py script you will see the osc messages in the Post window for bass, melody, and chords

////////////////////////////////////////////////////////////////////////////////////////////////
// This whole fucntion here is supposed to filter out the /status.reply messages, but doesn't...
(
f = { |msg, time, addr|
    if(msg[0] != '/status.reply') {
        "time: % sender: %\nmessage: %\n".postf(time, addr, msg);
    }
};
thisProcess.addOSCRecvFunc(f);
);

////////////////////////////////////////////////////////////////////////////////////////////////

(
OSCdef(\dinger,
    {
        |msg|
        {Pulse.ar(msg[1],rrand(0.01,0.5),0.3)!2 * EnvGen.ar(Env.perc,doneAction:2)}.play
}, '/test')
)


// stop posting.
thisProcess.removeOSCRecvFunc(f);

o.free;