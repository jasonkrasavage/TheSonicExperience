//Jason Krasavage
//Going to use some of the info on this link to figure out syncing osc messages with arguments and passing those into synthdefs etc.
//https://theseanco.github.io/howto_co34pt_liveCode/6-2-OSC-and-Data-Streams/

(
NetAddr.localAddr; //usually returns "a NetAddr(127.0.0.1, 57120)"

n = NetAddr.new("127.0.0.1", 57120); //redundant, can use "NetAddr.localAddr" instead

o = OSCFunc({ arg msg, time, addr, recvPort; [msg, time, addr, recvPort].postln; }, '/goodbye', n);

OSCFunc.trace(true); //lets you see the OSC stream for ALL ports (so it won't filter out the /status.reply messages, after running this and running the BlockParser.py script you will see the osc messages in the Post window for bass, melody, and chords
)
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
//Synth def that is being used in both osc definitions as of right now
SynthDef(\sines, {arg out = 0, freq = 440, release_dur, gate =1, amp = 0.2;
    var sines, env;
    env = EnvGen.kr(Env.asr(0.01, amp, release_dur), gate, doneAction:2);
    sines = SinOsc.ar(freq, 0, 2.2);
    Out.ar(out, sines * env);
}).add;
)

//second variation of sines working with envelopes to avoid popping. close but no cigar right now. It's better but the pop is definitely coming from ".free" in the oscdefs below. Need to sort that out
(
SynthDef("sinesTest", { |freq, out, gate = 1, attackTime = 1, decayTime = 1 sustainLevel = 0.5, releaseTime = 1|
    var env = Env.adsr(attackTime, decayTime, sustainLevel, releaseTime);
    var gen = EnvGen.kr(env, gate, doneAction: Done.freeSelf);
    Out.ar(out, SinOsc.ar(freq, 0, 0.5) * gen)
}).add
);

(
//OSC definition for handling triads. This def looks for messages sent from the "triad_send" python function
//will sustain until a new traid is sent
OSCdef.new(\sines,
    {

        |msg|
		~one.free; ~two.free; ~three.free;
		~one = Synth.new(\sines, [\freq, msg[1]]);
		~two = Synth.new(\sines, [\freq, msg[2]]);
		~three = Synth.new(\sines, [\freq, msg[3]]);
}, '/triad')
)

(
//OSC definition for handling a single tone. This def looks for messages sent from the "tone_send" python function
//will sustain until a new tone is sent
OSCdef.new(\sinesTest,
    {

        |msg|
		~tone.free;
		~tone = Synth.new(\sinesTest, [\freq, msg[1]]);
}, '/tone')
)
