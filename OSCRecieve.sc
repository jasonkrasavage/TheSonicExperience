// Patrick Tumulty
// Jason Krasavage
// The Sonic Experince SP19

(
//Run this first
NetAddr.localAddr; //Check listening port
n = NetAddr.new("127.0.0.1", 57120); // Run this to create net address object
o = OSCFunc({ arg msg, time, addr, recvPort; [msg, time, addr, recvPort].postln; }, '/goodbye', n);
)

(
//Run this second to monitor OSC messages in print window
f = { |msg, time, addr|
    if(msg[0] != '/status.reply') {
        "time: % sender: %\nmessage: %\n".postf(time, addr, msg);
    }
};
thisProcess.addOSCRecvFunc(f);
);



(
//Run this third
SynthDef(\sines, {arg out = 0, freq = 440, release_dur, gate =1, amp = 0.05;
    var sines, env;
    env = EnvGen.kr(Env.asr(0.01, amp, release_dur), gate, doneAction:2);
    sines = SinOsc.ar(freq, 0, 1);
	Out.ar([0,1], sines * env);
}).add;
)

(
//Run this fourth
SynthDef(\piano, { |out=0, freq=440, gate=1|
    var son = MdaPiano.ar(freq, gate, release: 0.9, stereo: 0.3, sustain: 0);
    DetectSilence.ar(son, 0.01, doneAction:2);
    Out.ar(out, son * 0.1);
}).add;
)

(
//Run this fifth
OSCdef.new(\triad,
    {

        |msg|
		~one.free; ~two.free; ~three.free;
		~one = Synth.new(\sines, [\freq, msg[1]]);
		~two = Synth.new(\sines, [\freq, msg[2]]);
		~three = Synth.new(\sines, [\freq, msg[3]]);
}, '/triad')
)


(
//Run this sixth
OSCdef.new(\noteOn,
    {

        |msg|
		t.free;
		t = Synth.new(\piano, [\freq, msg[1]]);
}, '/noteOn')
)
(
//Run this seventh
OSCdef.new(\noteOff,
    {
		t.free;
}, '/noteOff')
)


(
//Run this to manually stop chords
~one.free; ~two.free; ~three.free;
)