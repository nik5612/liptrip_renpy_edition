define narrator = Character(None, voice_tag="rino")
define rino = Character('Rino', color="#c8ffc8", image="rino", voice_tag="rino")
define chizu = Character('Chizu', color="#c8ffc8", voice_tag="chizu")
define woman = Character('Woman', color="#c8ffc8", voice_tag="others")
define yame = Character('Yame', color="#c8ffc8", voice_tag="others")
define honami = Character('Honami', color="#c8ffc8", voice_tag="others")
define writer = Character('Writer', color="#c8ffc8", voice_tag="others")
define photographer = Character('Photographer', color="#c8ffc8", voice_tag="others")
define editor = Character('Editor', color="#c8ffc8", voice_tag="others")
define colleague = Character('Colleague', color="#c8ffc8", voice_tag="others")
define noboribe = Character('Noboribe', color="#c8ffc8", voice_tag="others")


image side rino test = "images/heads/file_0132.cbg.png"


image bg white = "images/bgs/file_0000.cbg.png"

define patch = False

label start:
    stop sound

    play music "audio/music/file_0008.ogg"

    scene bg white
    with fade
    # белый экран
    # dissolve в розовые галюны
                
    voice "audio/voiсes/rino_file_0247.ogg"
    "My breath huffs out in uneven puffs."

    voice "audio/voiсes/rino_file_0248.ogg"
    "My pulse pounds and my head buzzes unpleasantly."

    voice "audio/voiсes/rino_file_0249.ogg"
    rino test "...Haah, mm... Ngh."

    voice "audio/voiсes/rino_file_0250.ogg"
    "The rough pants escaping my lips are at odds with the clinical office space."

    voice "audio/voiсes/rino_file_0251.ogg"
    rino "Haah... Haah..."

    voice "audio/voiсes/rino_file_0252.ogg"
    "I desperately clutch the folder to my chest as I stagger toward the wall. I shudder, and the papers scatter to the floor."

    play sound "audio/sounds/file_0000.ogg"
    "*rustle*"

    voice "audio/voiсes/rino_file_0253.ogg"
    "The sound of scattering paper and plastic reverberates in my ears. I dimly register the words on the meeting documents, crumpled by my sweaty hands."

    voice "audio/voiсes/rino_file_0254.ogg"
    rino "Haah, nngh... Haah."

    voice "audio/voiсes/rino_file_0255.ogg"
    "I tense my legs, fighting back syrupy moans."

    voice "audio/voiсes/rino_file_0256.ogg"
    "Heat pools in my stomach. My fingertips slide up my thighs."

    # тряска влево-вправо
    voice "audio/voiсes/rino_file_0257.ogg"
    rino "Ngh... Huh?"

    voice "audio/voiсes/rino_file_0258.ogg"
    "Just then, I catch a whiff of a fragrance like mint mojito.  I barely have time to take a breath before there are cool fingers on mine."
    
    voice "audio/voiсes/rino_file_0259.ogg"
    "Before I know it, I'm pressed up against the wall. The scent is so strong. Pleasure permeates my brain."

    voice "audio/voiсes/rino_file_0260.ogg"
    rino "...Boss?"
    
    voice "audio/voiсes/rino_file_0261.ogg"
    "As though in response to my syrupy moan, the fingertips heat up Her intense gaze shimmers like glittering sapphires."
    
    voice "audio/voiсes/rino_file_0262.ogg"
    "I swallow my moans as I give myself up to her."
    
    #dissolve in white
    #dissolve on black
    
    $ renpy.movie_cutscene("videos/liptrip_op_en.mpgv")
    
    show wide_bg at pan_right_stop

    play music "audio/music/file_0005.ogg"

    voice "audio/voiсes/rino_file_0263.ogg"
    rino "Whoa! This place is so fancy!"

    "Looking out from the glass-enclosed meeting room, the neat rows of desks and gleaming monitors are like something out of a TV show."
    "The workers are all dressed in a way that's somehow simultaneously casual and sophisticated."
    "Artfully placed decorative plants spread their lush leaves under the white lights."

    voice "audio/voiсes/rino_file_0264.ogg"
    rino "(So this is city life, huh?)"

    "It's a far cry from my previous workplace."
    "Having said that, I've been to countless offices for interviews."
    "While I'm taking in the unfamiliar atmosphere, a suit-clad woman enters the room with a laptop under her arm."

    #voice "voices/file_!!!!.ogg"
    woman "Sorry to keep you waiting."

    #voice "voices/file_!!!!.ogg"
    woman "Okay... Ms. Maiguma Rino. Digital media department, isn't it? I'll show you to your workspace."

    "Setting my lips, painted in my favorite coral pink lipstick, in a determined line, I get to my feet."
    "Taking a deep breath, I give a little nod to psych myself up."

    voice "audio/voiсes/rino_file_0265.ogg"
    rino "Okay!"

    #voice "voices/file_!!!!.ogg"
    woman "We operate a hot-desking system here. Next to the digital media section we have the marketing department."

    #voice "voices/file_!!!!.ogg"
    woman "Since there's some overlap in responsibilities..."


    "Ms. Sasahara from HR flips through the documents on her clipboard as she explains the rules of my new workplace."
    "While making appropriate noises to show that I'm listening, I glance around me."
    "New employees must be a regular occurrence, as no one pays me any heed, everyone focused on the work before them."

    voice "audio/voiсes/rino_file_0266.ogg"
    rino "(I guess the people who work at such a prestigious company wouldn't spare much thought for me.)"

    "Blinking my curled lashes, I keep a firm grip on the documentation I've been given. Feeling a little more grounded, I look around again."

    voice "audio/voiсes/rino_file_0267.ogg"
    rino "(I remember that slogan from commercials when I was a kid!)"

    "There's a wooden bookshelf filled with popular travel magazines, and familiar posters adorn the wall above them."
    "Excitement brings a smile to my lips, and I unconsciously step toward the display."

    voice "audio/voiсes/rino_file_0268.ogg"
    rino "(What am I doing?! I'm supposed to be listening!)"

    #voice "voices/file_!!!!.ogg"
    woman "Am I right in thinking you haven't worked in this industry before, Ms. Maiguma?"

    "Ms. Sasahara pushes back her short hair and eyes me up. I interviewed with someone else, but she's probably heard my work history from them."

    voice "audio/voiсes/rino_file_0269.ogg"
    rino "Uh, yes! Though I've always wanted to work in the travel industry."

    #voice "voices/file_!!!!.ogg"
    woman "Really? Well, the digital media department is desk work, so it won't be as challenging as working on location."

    voice "audio/voiсes/rino_file_0270.ogg"
    rino "O-Oh."

    "The brand-new digital media division at one of Japan's leading travel agencies is staffed by an elite few."
    "Or so I was told during the interview. Now I'm getting a slightly different impression from this woman, so I'm a little taken aback."

    #voice "voices/file_!!!!.ogg"
    rino "(I mean, I get that being a tour conductor is probably a difficult job, but, uhh...)"

    "Squashing my feelings, I follow Ms. Sasahara until she stops in front of a partitioned desk by the wall."
    "Then she calls out to a woman working nearby, gesturing toward the privacy partition."

    #voice "voices/file_!!!!.ogg"
    woman "Excuse me. Where's the editor-in-chief?"

    "The other woman pushes back her shaggy hair, responding that she's gone straight from a business trip to meet with a partner."
    "Then she adds that the boss mentioned she'd be back around the time HR would be finishing with onboarding for the new recruit."

    #voice "voices/file_!!!!.ogg"
    woman "Hah, of course. Those Alphas are always on the move."

    "Ms. Sasahara gives a knowing nod, though there's an exasperated tinge to her chuckle."
    #voice "voices/file_!!!!.ogg"
    rino "(Alphas...)"
    
    "I was already aware of this, but the word still automatically puts me on the defensive. Swallowing, I instinctively grasp the card holder hanging from my lanyard."

    #voice "voices/file_!!!!.ogg"
    woman "That should cover the office. Shall we get on with your induction while we wait for the editor-in-chief to return?"

    #voice "voices/file_!!!!.ogg"
    rino "Okay."

    #voice "voices/file_!!!!.ogg"
    woman "Oh, and we have a lot of female Alphas across the company, so... make sure you behave yourself."

    "Ms. Sasahara's eyes narrow even further. Though she spoke casually, there's a hardness behind her words, and I feel my eyebrow twitch."

    #voice "voices/file_!!!!.ogg"
    rino "Uh-huh. I'll do my best, within reason."

    "Of course, as a responsible adult, I have no choice but to force a smile and nod agreeably."

    #voice "voices/file_!!!!.ogg"
    rino "(ARGH! What the hell is her problem?!)"

    "Flopping face down on my desk, I splay my legs out. My boot heels clack loudly against the floor, but I don't care."
    "Raising my head, I suppress the urge to scream, settling for grinding my teeth instead."

    #voice "voices/file_!!!!.ogg"
    rino "Behave myself?! YOU behave yourself! Aren't you supposed to be HR?!"

    "My grumbles echo off the desk, bouncing back at me as though through a megaphone. My head buzzes with the reverberation, and I sigh."

    #voice "voices/file_!!!!.ogg"
    rino "(And then she spent ages showing me the copier and the kitchen, because I guess that's where I'm gonna be spending most of my time.)"

    "I'm getting more and more pissed off at Ms. Sasahara's attitude toward me."
    "I'm used to this kind of treatment, but I didn't expect it at my new place of employment."
    "I look at the documents Ms. Sasahara gave me and snort. Beneath my name is the word 'Omega', inscribed there like a brand."

    #voice "voices/file_!!!!.ogg"
    rino "And this editor-in-chief is supposed to be my boss, but she's not even here."

    "I've heard my boss is an Alpha, so I can already imagine what she's like: talented and beautiful, operating on another level to us Omegas."
    "At least, pretty much every Alpha I've encountered in my twenty-six years of life has been disgustingly perfect."
    
    
    
    
    #voice "voices/file_!!!!.ogg"
    woman "Oh, and we have a lot of female Alphas across the company, so... make sure you behave yourself."
    
    
    
    
    
    "Those words felt like a nail driven through me, pinning me in place. Recalling them makes me frown, gloom rolling up inside me."
    "Propping my chin in my hand and shaking my highlighted hair out of my eyes, I glare at the wall as though I can see through to the office on the other side."

    #voice "voices/file_!!!!.ogg"
    rino "(I heard they congregate in the big companies. Guess it's true.)"

    "In addition to biological gender, everyone is also assigned a secondary gender in one of three roles: Alpha, Beta, or Omega."
    "Most are born as Betas, but the Alphas, with their superior looks and abilities, are revered by society. Most of the prominent figures in every industry are Alphas."
    "In contrast, despite generally being attractive, Omegas like me have a history of oppression due to a particular trait we all share."
    "However, society is progressing with regard to the rights of Omegas, who have traditionally been discriminated against. Hence companies now being required to fill an Omega employment quota."
    
    #voice "voices/file_!!!!.ogg"
    rino "(Having an Alpha for a boss feels like a microcosm of society as a whole.)"
    
    "Thinking wryly to myself, I look down at the team's organizational structure chart at the bottom of my document pack."
    
    #voice "voices/file_!!!!.ogg"
    rino "Kiyotsu Chizu..."
    
    "Written at the top of the eight-person digital media team is the title 'Editor-in-Chief' and the name 'Ms. Kiyotsu.'"
    "As I'm flipping through the rest of the papers, there's a knock at the meeting room door before it immediately opens."
    "I tense up, expecting Ms. Sasahara, but instead it's one of the team members I was introduced to earlier."
    
    #voice "voices/file_!!!!.ogg"
    woman "The boss is back... Could you go pick her up?"
    
    #voice "voices/file_!!!!.ogg"
    rino "Pick her up?"
    
    #voice "voices/file_!!!!.ogg"
    woman "Yeah, since it's raining. She really should use the underground parking lot, but she always gets the cab to stop outside the building."
    
    #voice "voices/file_!!!!.ogg"
    rino "Oh."
    
    "Surely she can deal with getting a little damp?"
    
    #voice "voices/file_!!!!.ogg"
    rino "(I seriously have to go pick her up? She's not a kindergartner!)"
    
    "The woman quirks one manicured brow, the corners of her lips lifting."
    
    #voice "voices/file_!!!!.ogg"
    colleague "Besides, it's not like you're doing anything, is it?"

    "She laughs, and I feel my eyebrows fly up to my hairline. I force myself to smile brightly at the woman—Ms. Okayama, I think it was."
    "Then I jump up so vigorously, I almost flip the table."
    
    
    
    
    #voice "voices/file_!!!!.ogg"
    rino "Ugh, I am so PISSED OFF!"

    "I fume to myself as my boots ring out across the concrete floor. My hand tightens in a death grip around the random plastic umbrella I found in the office."
    "Squaring my shivering shoulders—I forgot my coat—I hurry along the mezzanine, trying to stay out of the rain."
    
    #voice "voices/file_!!!!.ogg"
    rino "(I don't care if she's my boss—I'm gonna give her a piece of my mind!)"
    
    "As much as it irritates me to have to complain to an Alpha, as my boss, she's the person I should take any complaints up with."
    "Coming to the bottom of the escalator, I walk out of the building and toward the side road where the taxis stop."
    
    
    
    
    
    "The road is mostly deserted. I stop in the doorway of the church next door to avoid the rain, clasping my card case as though to affirm it's still there."
    
    #voice "voices/file_!!!!.ogg"
    rino "(It's okay, I've got my meds, just in case.)"
    
    "After confirming that the six little pills are still inside, I take a deep breath to steady myself."
    "Sunset dyes the sky scarlet; the rain is a light drizzle. The street looks like it's been painted in shades of grey, and the dark suits of passing businesspeople are an inky black."
    "The light spilling from the office flickers like shrine lanterns. Breathing in the humid air, I close my eyes."
    "But the peace and quiet is momentary; the noise of an engine pulls me back to reality."
    
    #voice "voices/file_!!!!.ogg"
    rino "Aha, here she comes."
    
    "The growl of the engine rips away the calm as the taxi trundles to a stop. Peering through the window, I see a woman of a similar age to me."
    
    #voice "voices/file_!!!!.ogg"
    rino "(That must be her—the editor-in-chief, Ms. Kiyotsu.)"
    
    "It's gotta be her. The profile I spy through the window makes my breath catch in my throat; my instincts are telling me that this is an Alpha."
    "I approach the taxi and hold the umbrella out over the back passenger door."
    "The moment the door opens, words spill from my lips."
    
    
    
    
    #voice "voices/file_!!!!.ogg"
    rino "Um, Boss!"
    
    "My voice comes out strangled and hoarse. My breath stutters."

    #voice "audio/voiсes/rino_file_0000.ogg"
    chizu "Are you Ms. Maiguma?"

    #voice "voices/file_!!!!.ogg"
    rino "Yes! It's my first day, and..."

    #pink effect on
    "And what...? My thoughts melt away as my vision swims."
    "My cheeks are hot—not just my cheeks, my whole body. I can barely breathe. An ache spreads through my stomach, and the form of the women before me wavers."
    #pink effect off

    #voice "voices/file_!!!!.ogg"
    chizu "Don't tell me you're in heat..."

    "That's not possible... As the strength sags from my body, my boss leans out of the car."
    "Slim fingers curl over my hand on the umbrella, which falls from my grip as the woman supports me."

    #voice "voices/file_!!!!.ogg"
    rino "No. No, I can't be."

    #voice "voices/file_!!!!.ogg"
    rino "Just because I'm an Omega, that doesn't..."

    "I swallow again and again, holding back the moans that threaten to spill from my lips."
    "How could I go into heat now of all times?!"
    
    
    
    
    #voice "voices/file_!!!!.ogg"
    rino "(It's not possible!)"

    "Omegas periodically go through a phase called 'heat' where we're unable to control our sexual impulses."
    "During that time, we're in a constant state of arousal, our thoughts consumed by sexual urges... Just like how I'm feeling right now."

    #voice "voices/file_!!!!.ogg"
    rino "(I have to get away... She's an Alpha!)"

    "Holding the umbrella over us, my boss regards me with a frown. There's a fire in her eyes that calls to me."

    #voice "voices/file_!!!!.ogg"
    rino "(If I stay here, she'll claim me...)"
    "There's a fire in my belly and a flush creeping up my neck. Trying to fight against my instincts, I put my hand to my neck, my nails digging into the skin."

    #voice "voices/file_!!!!.ogg"
    chizu "Yes. Yes, my apologies. Please don't worry about it."
    
    
    
    
    
    "I vaguely hear her talking with the taxi driver as I lean against the taller woman, who has an arm wrapped around my shoulders."

    #voice "voices/file_!!!!.ogg"
    chizu "Oof. Can you walk?"

    "Her voice reverberates by my ear as her cool fingers curl around my shoulder."

    #voice "voices/file_!!!!.ogg"
    rino "Ah... No... Don't bite me."

    "My voice is hoarse."
    "My boss purses her lips slightly then removes her arm from my shoulder, instead taking hold of my clammy, dangling hand."

    #voice "voices/file_!!!!.ogg"
    chizu "At the very least, we need to get you somewhere private."

    #voice "voices/file_!!!!.ogg"
    rino "Haah... Ah."

    "A scent of sweet honey and refreshing mint wafts over me, growing stronger as I lean in toward it."

    #voice "voices/file_!!!!.ogg"
    chizu "Do you have your suppressant?"

    #voice "voices/file_!!!!.ogg"
    rino "Ah... Yes."

    "Over her shoulder, I can see other people around us, and their gazes make me shiver."

    #voice "voices/file_!!!!.ogg"
    rino "(I can't believe it. I'm really in heat right now.)"

    "I must be giving off Alpha-attracting pheromones. Just the thought of a passing Alpha forcefully claiming me makes my chest blaze uncomfortably."
    
    
    
    
    #voice "voices/file_!!!!.ogg"
    woman "Oh, and we have a lot of female Alphas across the company, so... make sure you behave yourself."

    "Those words from earlier come back to me. I bite down on my tongue, fighting desperately to stay in control, and grimace at the dull pain."

    #voice "voices/file_!!!!.ogg"
    rino "(I need to take that pill, stat!)"

    "Pushing her away, I grab the pass holder hanging around my neck and frantically pull out a pill."
    
    
    
    
    
    "I toss it into my mouth and swallow. Once the bitter taste passes, I sigh."

    #voice "voices/file_!!!!.ogg"
    rino "No way..."

    "Usually, my symptoms would lesson within seconds of taking the medicine, and my heat would subside a few minutes later. But this time, my heart continues to pound."
    "The miracle medicine we Omegas rely on to suppress our heat... isn't working."

    #voice "voices/file_!!!!.ogg"
    rino "(What am I gonna do...?)"

    #voice "voices/file_!!!!.ogg"
    chizu "Come here."

    "Her voice quivers as she takes me by my trembling hand. I'm powerless to resist, unable to do anything but moan at the feel of her cool fingers on mine."
    
    
    
    
    
    "When we reach the elevator, my boss folds up the umbrella and slams the button for going up."
    "As soon as it arrives, she hustles me inside."
    "The second the door closes, she turns to me. Her gaze is heated; her fingers on mine are cool. She hasn't pressed a floor button."

    #voice "voices/file_!!!!.ogg"
    chizu "I'll contact the building security office."

    "When she makes to leave the elevator, my body moves automatically."

    #voice "voices/file_!!!!.ogg"
    chizu "Ngh... What?"

    "I wrap my arms around her neck and lean back against the wall, pulling her into me."
    "There's confusion in her eyes, and I grit my teeth. My head is spinning from her Alpha scent as I fight to think clearly."

    #voice "voices/file_!!!!.ogg"
    rino "(I can't believe I can't suppress my heat. This is crazy.)"
    
    
    
    
    
    #h scene 1

    #voice "voices/file_!!!!.ogg"
    rino "No..."

    "My hoarse voice echoes around the elevator. My boss's eyes widen in surprise, but she stays silent, listening to me intently."

    #voice "voices/file_!!!!.ogg"
    rino "It'll just confirm what they already think, that Omegas are useless... Haah."

    "I feel something rising in my burning belly. I hate how my body is reacting to nothing at all."

    #voice "voices/file_!!!!.ogg"
    rino "(This is my dream job... How can this be happening on my very first day?!)"

    "My body is burning up, my chest is tight, and tears slide down my cheeks. Yet I still plead fervently with my boss."

    #voice "voices/file_!!!!.ogg"
    rino "So please, ah, don't tell the company."

    #voice "voices/file_!!!!.ogg"
    chizu "That's not..."

    "Her voice is small and trembling, unlike what I'd expect from an Alpha. The lack of conviction in her tone makes me swallow."

    #voice "voices/file_!!!!.ogg"
    rino "You're an Alpha, aren't you?"

    "Being an Alpha means she could sink her teeth into my neck to claim me. Once claimed, an Omega won't come into heat for anyone but the Alpha who claimed them."
    "But that also means never being able to choose another partner."

    #voice "voices/file_!!!!.ogg"
    rino "(If she bites me, this will all stop.)"

    "My tears fall as I wrap my arms around the taller woman. Her eyes widen, her trembling lashes casting shadows over her irises."

    #voice "voices/file_!!!!.ogg"
    chizu "Mmph, haah..."

    #voice "voices/file_!!!!.ogg"
    rino "Haahm... So hot... It's too much..."

    "Panting, I pin her pale eyes with mine."
    "My head aches, and my thoughts are in chaos. My lungs feel like they're about to burst, and my heart pounds like it's going to leap out of my chest."

    #voice "voices/file_!!!!.ogg"
    chizu "Haah."

    #voice "voices/file_!!!!.ogg"
    rino "Aah... Please..."

    "Her eyes give me no clue to her emotions, but she lets out a pained sigh. Then she pushes me against the wall."
    
    
    
    
    
    chizu "Close your eyes."
    "My heart skips a beat."
    "I freeze at her commanding tone and her gentle hand on my waist. Burying my face in her sideswept hair, I nuzzle my cheek against her neck."
    rino "(This scent of hers... excites me.)"
    "As I drink in her scent, her hand slides upward. There's a metallic snap, and the pressure in my chest eases."
    rino "(Ah... My bra.)"
    "In a daze, I press my hips forward."
    "Even through the fabric of our clothes, the softness of her thighs sets me alight."
    rino "Ahmph..."
    chizu "Sorry to put you through this."
    rino "Mmph."
    rino "(Her touch is so gentle.)"
    "Her soft, hot body wraps around me, radiating heat. It feels so good, and her sweet breath makes my stomach melt."
    "Her fingers find their way beneath the hem of my blouse, tracing my abdomen. When they brush my breasts, my shoulders twitch."
    chizu "Does this feel good?"
    "She whispers sensually as her fingertips dance over my nipples. The lightness of her touch is frustrating, and I tighten my arms around her neck."
    rino "Nngh. Yes, it feels good."
    chizu "Fwaah... Good."
    rino "(Her scent is getting stronger.)"
    "Engulfed in her sweet scent, my hips buck. The place between my legs tingles with heat and my bangs stick to my sweaty skin."
    rino "Ngh, haah."
    "I moan and cling tighter to her. Just then, I feel a swoop of buoyancy as the elevator jerks to life."
    chizu "Honestly. You wouldn't usually be so lucky."
    rino "Ah, aahn!"
    "Despite her grumble, she embraces me tightly. When the tip of my nose brushes her hair, I catch a whiff of petrichor."
    "She presses up against me as she gently pinches my nipples. The wall is cold at my back while her hot scent smothers me, its sweetness making my head spin."
    
    
    
    
    
    rino "Mm, aah. Boss, I—aah!"
    "The sound of a kiss reverberates in my ear. Her tongue traces my lobe, and a shudder of pleasure runs down my spine."
    chizu "Come for me."
    rino "Ah!"
    "She bites down gently on my earlobe, and my stomach tenses. My hips quiver, but my thighs are pinned in place."
    rino "Ah, nngh... Haah, mmph. Yes...!"
    chizu "Haah, mmph."
    
    
    
    
    
    "I cling to her as the aftershocks shudder through me. Hot breath grazes my neck, but then her body heat withdraws."
    chizu "Lift your arms."
    rino "Haah... Huh?"
    "My boss picks up my discarded bra and deftly hooks it around my back. Then she pulls my blouse down and smooths it out."
    rino "(Huh? Has my heat abated?)"
    "My body is cooling down, my logical senses returning. I look up at my boss, but it's at that moment that the elevator comes to a stop."
    "The door slides open to reveal two women dressed in business casual. I hurriedly straighten my posture as my boss leads me by the hand out of the elevator."
    rino "(Huh? She didn't bite me.)"
    "I put my hand to my shoulder, but there's no burning bite mark. Feeling a little deflated, I dazedly run my hand over the skin as it cools in the autumn air."
    rino "(She didn't claim me, but she did make me come, so I guess that's why it's abated.)"
    "I recall a line from a textbook: 'When faced with an Omega in heat, an Alpha will lose control and seek to bite their neck to claim them.' My gaze drifts to our joined hands."
    "Fine veins stand out on the back of the pale, delicate hand poking out of her coat sleeve."
    
    
    
    
    
    rino "Um, thank—"
    chizu "Looks like the rain's let up."
    rino "Huh? Oh, so it has."
    "I glance up at the sky. The elevator leads to the outside entrance area covered by a roof that's beaded with raindrops."
    chizu "That's all for today. Go back to the office."
    rino "Uh..."
    "Her cool, detached tone feels like a rejection. My boss turns away from me, putting a finger to her lips."
    chizu "In fact, you can head home early today."
    rino "Um..."
    "With those cold words, she pushes the umbrella at me. I reflexively take it and she moves away, brow furrowed."
    chizu "We won't be able to avoid one another entirely, but you should stay away from me."
    rino "Uh...?"
    "Then she hurries off, as though she can't wait to get away from me. I stand rooted to the spot, gazing after her departing figure."
    rino "What's with her?"
    "Stay away from her? Her demand gives rise to simmering, complex emotions within me."
    rino "(And here I was thinking she was a nice person.)"
    "Thinking back on what we were just doing, I press my hand to my chest. I bite my lip as her cold tone lingers in my mind, replacing the sweetness of earlier."
    "Tasting lipstick in my mouth, my hand tightens around the umbrella handle."
    "Is this because I'm an Omega?"
    rino "(I guess I'll just have to get on with it and do my job.)"
    
    
    
    
    
    "Resolving this to myself, I start to walk toward the building. The sky above glows blue between the skyscrapers, and the sun is starting to sink behind the concrete jungle."
    rino "(But why didn't my heat suppressant work?)"
    "Questions run through my mind, and I reflexively grip my card holder. My pulse has slowed and my body is back to its normal temperature."
    rino "Crap, I'd better get back to the office!"
    "If I linger much longer, they'll think I'm slacking off."
    "I start to jog, hurrying toward the security gate."

    ###

    "Tap, tap, tap."
    "My fingers clack rhythmically across the keys, followed by a satisfying click as I press the send button."
    "Letting out a small sigh toward the screen, I chew my lip as I stare at the schedule."
    rino "(Hmm. I should probably email the writer.)"
    "Judging by the schedule, I really need to check on the progress of the manuscript."
    "I've been working here for a month now, and in that time I've got a handle on each writer's idiosyncrasies; or rather, how well they can stick to a deadline."
    woman "Do you have a minute, Ms. Maiguma?"
    rino "Oh, sure. What is it?"
    "I shift my gaze away from the screen and toward my colleague."
    "It's Ms. Yame, the article editor. She's got her planner open as she regards it thoughtfully."
    yame "It's about the article on the hedgehog cafe..."
    rino "I already contacted them and set up an appointment."
    rino "I've added it to your calendar, so it should be on there."
    "Ms. Yame nods, looking relieved to hear my answer."
    "After I relay my conversation with the store manager to her, she thanks me and returns to her desk."
    rino "(Let's see... I've made appointments with all the places we're due to write about. Next I'll aggregate the survey responses.)"
    "The digital media department I belong to runs a tourism website called 'Fuller' that has daily articles on recommended sight-seeing spots."
    "Now that I've settled into the job, I can anticipate what needs to be done. It's a lot, from scheduling appointments to reviewing the articles sent in by our writers."
    rino "(Still, it's enjoyable work. Oh, I proofread the article about this art gallery, and someone decided to visit it!)"
    "I let out a little sigh as I run my eyes over the survey responses then take a sip from the mug atop my desk."
    rino "Haah."
    "Savoring the mellow flavor of lukewarm milk tea, I stretch in my seat to loosen up."
    "Just then, the woman who sits opposite me pops her head up over her monitor."
    rino "Is something wrong?"
    honami "Mm, I'm kinda stuck. These samples I got from the designer are both pretty good, but neither is grabbing me more than the other."
    "I get up and peer at her screen. There are two designs for the upcoming special site we're hosting about winter camping, and both are clear and vibrant."
    rino "Hmm. I think you should go with your gut."
    honami "Right..."
    rino "But if you're having trouble, maybe you could bring it to the editor-in-chief?"
    "Going back to my own computer, I pull up the team's shared calendar. I check Ms. Kiyotsu's schedule then call out to Honami."
    rino "She's between meetings right now, so she should have time."
    honami "Really? Great, I'll go talk to her."
    "Honami heads off to the boss's desk. Ms. Kiyotsu sits in the shadow of an ornamental plant, so I only catch a glimpse of her profile."
    rino "(Though she's frosty toward me, she seems like a really nice boss to everyone else.)"
    "Ms. Kiyotsu stops what she's doing and gets up to make eye contact as she talks with Honami. From time to time, a smile crosses her face."
    rino "(She's barely spoken to me since that day...)"
    "I frown as I recall her parting words to me on my first day on the job."
    rino "Stay away from her, huh?"
    "Alphas are the privileged class, and many of them detest Omegas, or see us as a subclass. Still, it's the first time I've experienced such treatment directly."
    "Yet despite that, when it comes to work, she takes a generally relaxed attitude, and she's smiling at Honami right now."
    "I watch as she tucks her long hair behind her ear and her cheeks dimple slightly."
    rino "(It's not fair for her to look so cute when she smiles.)"
    "I find myself grimacing at the sight of her reacting with enthusiasm to Honami's ideas."
    rino "(She does converse with me normally when it's about work, but...)"
    "Her overall demeanor is still icy."
    "If I abruptly show up at her desk, she'll casually put distance between us. When I brought the cardigan she'd left in a meeting room, she made no move to put it on."
    rino "I feel like a dad whose teenage daughter's going through her 'I hate authority' phase."
    "I'm working myself into a froth thinking about my boss's attitude when Honami comes back. She's smiling, and I can practically see the light bulb over her head."
    "I'm glad to see her looking energized. At the same time, I see a notification on my screen, reminding me of the next meeting."
    rino "Oh, I'd better get to the meeting."
    
    
    
    
    
    "I hurriedly tidy my desk and close my laptop. Then I drop my mug off at the sink and hurry to the meeting room."
    
    
    
    
    
    chizu "Today will be a brainstorming session, but we'll also give deeper consideration to any ideas that really click."
    "The editor-in-chief turns to the information displayed on the giant screen on the wall."
    "Beside her, Ms. Noboribe, who is in charge of collating proposals for articles, is taking notes."
    chizu "Can I hand it over to you, Ms. Noboribe?"
    "These regular planning meetings are all-hands, including not just editors, but members of the design and sales teams, too."
    noboribe "The New Year's feature will include pieces on the illuminations, as usual..."
    "She taps at her computer, displaying articles from the previous year on the big screen as she starts to explain this year's travel industry trends."
    rino "(Hmm... Ideas for features...)"
    "I still don't have huge confidence in it, but I have come up with something inspired by last year's articles and other media I've been following."
    "Seemingly so have all the other editors, as everyone starts to pitch their ideas after Ms. Noboribe finishes her explanation."
    chizu "A feature on Kyushu's hotpot dishes? Hmm. Tomato and garlic hotpot? Sounds good. This place is close to a major train station; could you incorporate it into an itinerary?"
    colleague "Good idea. I'll do some more research for the next meeting."
    chizu "Great. Next we have... Ms. Maiguma."
    "The editor-in-chief suddenly says my name, smiling encouragingly even as she keeps her gaze fixed on the screen. Feeling everyone's eyes on me, I gulp."
    chizu "Do you have any ideas?"
    rino "...I do!"
    rino "How about a special feature on Hokuriku based around the theme of matchmaking?!"
    chizu "Matchmaking...?"
    "Removing my hands from my keyboard, I straighten my posture and take a deep breath before continuing in as calm a voice as I can manage."
    rino "I've seen that some of the popular shrines have redesigned their omamori charms. They're super cute!"
    "I pull up some pre-prepared images on my screen and show it to the others."
    "Honami, who's also a designer, squeals that they're adorable, and the sales department nod. Beside them, the editing team also look pleased."
    editor "Yeah. I bet they'd appeal to foreign visitors, too."
    rino "Yes! There are plenty of direct flights into Hokuriku..."
    "Just then, my eyes meet Ms. Noboribe's. Her expression is slightly twisted, and she cuts me off."
    noboribe "Matchmaking? Not all of us are obsessed with mating, you know."
    "I abruptly shut my mouth, and Ms. Noboribe goes on."
    noboribe "Perhaps girls like you care about matchmaking, but Betas like myself fall in love the usual way, so it's hard to relate."
    rino "(Girls like me?)"
    "At the meaning behind those words, my chest aches like a fist has closed around my heart. I look around the table, but everyone else remains close-lipped."
    rino "Matchmaking isn't just about mating..."
    editor "Right."
    "The Editor cuts in placatingly. Pushing her wire-rimmed glasses up her nose, she looks down at her documents."
    editor "Though the majority of our user base is over the age of forty, so I'm not sure the theme would resonate with them."
    editor "What do you think, Ms. Kiyotsu?"
    chizu "Hmm."
    "The editor-in-chief drums her fingers on her lips, regarding me and Ms. Noboribe through narrowed eyes. My pulse speeds up under her gaze, and I feel my cheeks grow hot."
    "I hug my folded arms around myself as I wait for her response. Eventually, she lowers her hand and looks at me."
    chizu "Mm. It's a rather trite theme, so it's not viable in its current form."
    rino "Oh..."
    "My shoulders droop, and I bite my lip. I look back at the editor-in-chief, but her expression remains unreadable."
    "With that, the deputy editor takes over and finishes up the meeting. It's decided that everyone will summarize their ideas and present them at the next meeting."
    
    
    
    
    
    "The meeting finishes late, so my coworkers are in a rush to leave and get home."
    "I watch them go as I slowly pick up my coat and shove my laptop into my bag."
    rino "(She said that it won't work in its current form, but doesn't that mean it has a chance if I refine it.)"
    "At least, judging by the initial reactions to my suggestion, it's not fundamentally a bad idea."
    "Still, Ms. Noboribe and the Editor were right in their criticisms."
    "A trite theme."
    "Thinking back on those words, I bite my lip."
    rino "(She's right. Our readers aren't gonna care if it's only about charms for matchmaking.)"
    rino "...I've got this."
    "I put on my coat, say goodbye to Honami, and sling my bag on my shoulder."
    rino "See you tomorrow!"
    "I speak loudly enough for my boss to hear, then hurry out of the office."
    rino "(I've gotta come up with a plan that everyone will like by the next meeting!)"
    "I nod to myself to affirm my resolution."
    "I want to prove that I can do this."
    "And that it has nothing to do with being an Omega or a Beta or whatever."

    ###

    "I gaze vacantly out through the window, watching the lights of the business district glitter across the ground. Then I glance at the clock on the wall."
    "It's after 7 PM. There're a few people left in the office, but no one at the desks near me, so I feel comfortable enough to stretch my arms up and crack my back."
    rino "Hngh. Almost there."
    "Slides are lined up on my screen with notes for my pitch below."
    rino "(Yeah, this is pretty good! I'm a damn genius!)"
    "I fold my arms, tap my finger on my lip, then give a little nod."
    "I've added statistics from market analysis and past article trends and reworked the content. It's pretty different to my original pitch, but I'm happy with how it's turned out."
    rino "(I should go over the presentation again.)"
    "It's been tough working on this alongside my daily duties, but I'll be able to relax once tomorrow's meeting is over."
    "I steel myself to get back to work then grab my mug for a swig of pick-me-up."
    rino "...Ugh, I'm out."
    "I stare down into the empty mug then get up and head to the drink corner."
    "I slide my cup into the slot in the coffee machine and press the button."
    "As I watch the billowing steam, my stomach rumbles pitifully."
    rino "...I'm starving."
    "I realize that I haven't eaten since I started working on the presentation."
    rino "(I'll go pick something up at the convenience store.)"
    "I know that the hungrier I get, the less I'll be able to concentrate. I pick up my cup of coffee and am about to head to my desk when I see a familiar figure."
    honami "You're working hard today."
    rino "Oh, you're still here?"
    "It's Honami, with Ms. Yame from the editing team behind her. They're both wearing their coats and carrying their bags."
    rino "I thought you'd left already."
    honami "We did, but since we heard you were still here..."
    "Honami raises a hand that's holding a paper bag decorated with a botanical print."
    yame "Thought you could use a snack. We were told that something sweet'd give you a boost."
    rino "Ooh, fruit sandwiches?"
    "I open the box inside the bag to find a neat arrangement of fruit sandwiches and some mini trifles."
    rino "Wow! Thank you so much! I was just starting to get hungry."
    "My stomach rumbles at the sight of juicy strawberry and mango pieces enveloped in cream between sweet bread slices. Honami and Ms. Yame exchange a look and giggle."
    honami "You really love sweets, huh?"
    rino "Yeah, I do! Ooh, which should I have?"
    rino "Oh, can I get you a drink?"
    "I set the paper bag down on my desk then go back to the drink corner and grab some paper cups."
    yame "It's okay, I can get my own. Besides, aren't you in the middle of something?"
    rino "Oh, right..."
    "My hand stills as I abruptly realize why they've returned to the office at this time."
    "Honami looks over at my desk, her brow furrowing apologetically."
    honami "Sorry I didn't back you up in the meeting. Honestly, I've been wanting to help you out this whole time..."
    rino "(She's concerned about me.)"
    "Sometimes, I'll catch Honami's eye during work. I always smile back at her, but now I wonder if she was looking out for me."
    "She must've been too scared to be friendly with me in front of Ms. Noboribe and the deputy editor-in-chief, but today she's come back to the office after work for my sake."
    rino "(I really appreciate that.)"
    "I nod, staring thoughtfully at her."
    rino "Not at all. I'm really happy you're here now."
    "I tell her my honest feelings then flash her a grin. Honami sighs with relief and smiles back."
    yame "And I've been wanting to see your pitch."
    rino "Oh, then it'd be great if you could take a look at my presentation! I'd love to get your feedback on it."
    yame "Of course. It's only fair considering how much you always do for me."
    "With the fruit sandwiches and cup of coffee in hand, I head back to my desk and open my laptop."
    
    
    
    
    
    "I lay the sandwiches out on the table, and we all grab one. Ours is the one spot of light and laughter in the otherwise dim office."
    rino "Mm, this is so good."
    "I take a bite and smile around the sweet taste of strawberry and buttery cream."
    honami "Isn't it?! I had no idea there was such a good patisserie so close to the office."
    rino "Yeah. I've gotta check it out!"
    
    
    
    
    
    "As I lick cream off my fingers, I find my head clearing."
    "I wolf down the sandwich in no time and clean my hands with a wet wipe. Then I look at my screen as I chow down on seconds."
    
    
    
    
    
    rino "So, about my pitch..."
    "The other women join me in looking at the screen, and I start to explain."
    rino "I stuck with the theme of matchmaking, but I kinda shifted the perspective..."
    "With the sandwich in one hand, I take them through the plan page by page, looking to Honami for her reactions. Ms. Yame peers over my shoulder while she eats a trifle."
    honami "This is so much better!"
    yame "Yes. You've done a great job."
    "I'm relieved to hear this. Honami reaches over and moves the slideshow back, eyes narrowed thoughtfully."
    rino "Was there an issue?"
    honami "Hmm. Ah, right, this photo here."
    rino "I just grabbed that one off the internet, but maybe it's not a good fit?"
    honami "It's fine, but I think there's a better one in the stock portfolio. Hang on a sec."
    "Honami grabs her own laptop from her locker and sends me a photo. Meanwhile, Ms. Yame points to the slide currently on screen."
    yame "It might be a good idea to vary up your page structure, too. Like maybe change pages 3 and 5, add some additional sections?"
    rino "Oh, that's a great idea. I wouldn't have thought of that."
    yame "Well, I've been in the project pitching trenches for a decade."
    "I make adjustments to my materials as they give their opinions and point out things I never would've noticed on my own. I'm having fun, and my fingers fly over the keys."
    
    
    
    
    
    "Once I've finished the adjustments, Ms. Yame looks over the slides again. There are faint lines around her eyes as they crinkle with a kindly smile."
    yame "You know..."
    rino "What is it?"
    yame "About what Ms. Noboribe said."
    "I automatically tense at her name."
    
    
    
    
    
    noboribe "Perhaps girls like you care about matchmaking, but Betas like myself fall in love the usual way, so it's hard to relate."
    
    
    
    
    
    rino "(Omegas have normal relationships, too.)"
    "That's what I wanted to hit back with, but I swallowed my words. Recalling it now, I again feel like there's something lodged in my throat."
    yame "As a director, she tends to get bogged down in the numbers, but we both just want to put out the best articles we can."
    "The conviction in her tone makes me draw in a sharp breath."
    "Until now, I've never really thought about how hard other people in the company must be working."
    rino "(But even so, she didn't have to say it so nastily.)"
    yame "Still, she shouldn't have said it like she did. She didn't have to bring her own subjective ideas and experiences into it."
    "Ms. Yame says exactly what I was thinking, and I chuckle. Wiping at my eyes, I nod."
    rino "Right. Yeah. I'll do my best!"
    
    
    
    
    
    "When I notice that the clock on my computer reads, I close my open tabs."
    "Everyone else in the department is long gone; the only desks still lit are mine and Honami's."
    "I stow my laptop in my locker, grab my coat, and approach Honami."
    rino "(She stayed with me the whole time.)"
    "I call the elevator, and we get in together."
    
    
    
    
    
    "We chat about tomorrow's meeting and other office gossip. Then, as we're passing through the security gate, Honami suddenly addresses me."
    honami "How come you didn't change the matchmaking theme?"
    rino "Huh?"
    "For a moment, I'm taken aback by her question."
    "Maybe it would've been easier just to change it, since it's not really a theme that Ms. Noboribe or the others can really relate to."
    rino "(But...)"
    "I clutch my card holder as we walk."
    "I sensed the thorniness in Ms. Noboribe's words. And I understand the reasons behind it."
    rino "I guess I felt like if I changed it, people would see it as proof that Omegas only think about their destined mate, and I'd hate that."
    "I ball my hand into a fist and thrust it forward. It annoys me that people think that all an Omega wants in life is to meet the other half of their fated pair."
    "Honami laughs at my shadow boxing. Then she inclines her head slightly so she can peer into my face."
    honami "But all Omegas do have a destined mate, right?"
    "A destined mate."
    "Another person with whom you have perfect genetic compatibility, and who you're drawn to by a primal instinct."
    "You're attracted to them the instant you meet, and you're also supremely sexually compatible."
    "It was all explained to us during middle school, but..."
    rino "Uh, well, I guess. But meeting them would be a one-in-a-million miracle."
    honami "But you know as soon as you lay eyes on them, right? That's so romantic."
    rino "I think you've watched one too many TV shows."
    honami "I love the idea of it, but... I think I'd spend every moment wishing I could meet them."
    rino "Mm, you think so?"
    "I've never really thought about it, but I guess I do have a destined mate somewhere out in this big wide world."
    rino "(Still, I probably wouldn't notice if I passed them by in such a busy city.)"
    
    
    
    
    
    "The cold winter wind pierces my skin, and I pull my coat around me. Looking up at the sky, I can see the red light of Tokyo Tower glowing between the buildings."
    "As we head in the direction of that light, we talk about what tomorrow's workday will bring."

    ###

    rino "Fwaah..."
    "Stifling a yawn, I close my laptop and shut off the power. The planning meeting is due to start at AM, right at the beginning of the work day."
    "I've arrived early, but there's nothing left to do on my presentation, so I just checked my emails. Now I stretch my fingers out."
    "Looking around, I see that I'm the only one here. The office feels nice, enveloped in the cool, clear light of early morning."
    "With nothing else to do, I crouch down next to a nearby ornamental plant and mist it."
    rino "Hm hm hm. Hm hm hmmm."
    "Humming a tune I picked up from social media, I'm spraying in time to the melody when I suddenly hear a voice behind me."
    
    
    
    
    
    chizu "Morning."
    rino "Eep!"
    "I drop the bottle in suprise then scrabble to pick it up. Setting it back in its place, I see the editor-in-chief putting down her coat and bag at her desk."
    
    
    
    
    
    rino "Good morning!"
    rino "(She scared me!)"
    "In the shadow of the plant, I watch her over her desk partition."
    "But she feels my eyes on her and quickly averts her gaze."
    "Then she swaps her coat for the blazer that was draped over her chair, shrugs it on, and heads to the drinks corner."
    rino "(I wonder if she arrives this early every day.)"
    "According to Ms. Yame, our boss is a surprisingly hard worker. Although she's an editor, she also acts as a salesperson, generating us a lot of leads."
    rino "(Hehe. Bet you'd never catch her yawning at her desk like me.)"
    "It's not yet 8 AM, but she's as cool and composed as ever, without a single crease in her clothes. Yet, as I watch her pour herself a coffee, she looks like any other office worker."
    rino "(She told me to stay away from her, but surely she won't mind a quick chat... Let's do it!)"
    "I hate feeling like I'm walking on eggshells around her."
    "Screwing up my courage, I call out to my boss."
    rino "There are some leftover sandwiches from yesterday in the fridge—would you like one?"
    chizu "No thanks. I'm not a fan of fruit."
    "She flatly turns down my offer then heads back toward her desk with a paper cup of coffee in hand."
    "I stare after her, wide-eyed."
    rino "How did you know what kind of sandwiches they are without looking?"
    "Did she take a peek into the fridge in the kitchenette before coming here?"
    rino "(No, why would she do that?)"
    "My boss's shoulders twitch at my question. She turns back to me, brows furrowed."
    chizu "I, uh..."
    rino "Did YOU buy the sandwiches?"
    "Thinking back on it, Honami and Ms. Yame didn't seem familiar with the store they came from."
    "My boss puts her hand to her cheek, her eyes darting around nervously. Seeing her like this makes me feel agitated, too, and I twist my fingers together."
    rino "Why would you do that?"
    chizu "I bumped into Honami and Ms. Yame on my way home last night. They were wondering whether to go back, so I gave them a reason to. That's all."
    "That's not what I was asking, but never mind. The editor-in-chief sighs, her expression conflicted."
    chizu "Did you finish your pitch?"
    "She glances at my laptop."
    rino "Oh, uh, yes. Here it is."
    "Still reeling from this revelation, I open my laptop and bring up my presentation. My boss takes the machine from me and regards the screen intently."
    rino "(Should I say something?)"
    chizu "Hm."
    rino "(She's taking this super seriously.)"
    "Sneaking a peek at her profile, I see the light of the screen reflected in her eyes. I press my lips, colored with a mauve pink, into a line."
    "She takes the time to look at each page, and my heart rate speeds up every time the screen changes. I wait with bated breath until she finally arrives at the last slide."
    rino "Um... What do you think?"
    "Clutching the hem of my skirt, I screw up my courage to ask. My boss smiles."
    chizu "It's a good approach."
    rino "Ah! Really?!"
    chizu "This part here: 'Are you looking for your meet-cute?' That's great."
    "Without thinking, I lean toward her so we can look at the screen together. She's on the page where I summarize the concept of my article pitch."
    "I've outlined an article about the fun of randomly discovering new places during your trip; it's not simply a list of ideas, but more like a how-to article."
    "My boss smiles slightly and, commenting that it's different to your average travel guide."
    chizu "I like how you've included an itinerary that starts with the shrine you suggested at the first meeting."
    rino "Oh, Honami helped me with that slide."
    "She smiles again as I glow with pride; but then her expression clouds over slightly."
    chizu "But if you're going to work overtime, you need to let me know first."
    rino "Oh. Okay!"
    "I nod reluctantly, and the editor-in-chief gives me a concerned look."
    chizu "Also, I'm not saying I won't approve it, but you shouldn't be taking work home with you. I'm saying this for your own sake."
    rino "(She's looking out for me, too.)"
    "My boss is regarding me intently, as though checking my face for signs of ill health."
    "I'm overjoyed by her consideration, and my chest constricts with an odd, restless sensation."
    "My pulse speeds up, and I find myself staring back at her."
    "Her slim fingers run through her hair, and she narrows her eyes at me, uncomfortable under my gaze."
    rino "(I've got butterflies.)"
    # pink_effect on
    "My heart pounds; my chest feels tight."
    "My cheeks burn; my breath comes out hot and moist."
    rino "(Why am I so happy about this?)"
    chizu "...Ms. Maiguma!"
    "I catch a whiff of scent, and then my boss's arms are around me. My vision wavers."
    rino "Mm... Huh?"
    "Is this my heat?"
    "Before I know what's happening, I'm being led away."
    rino "Um, what about the pitch...?"
    "I can barely think or speak. My brain feels like it's on fire while my face flushes and my breathing grows ragged. Her fingertips burn on my waist."
    chizu "Haah... You're such a nuisance."
    "Tears well up in my eyes."
    rino "Sorry... I..."
    "My body is on fire. I cling to my boss, nuzzling against her neck. Her soft body and her distinctive Alpha scent makes my head spin."
    chizu "Don't give me that look."
    
    
    
    
    
    # pink_effect off

    "Her voice sounds strained. She's practically carrying me now, and I give my body over to her strength and let her walk me out into the corridor."
    "Slam."

    "In the dim meeting room, she sits me down on a chair. I gaze blankly ahead as she turns her pale face to me. There's an impatient gleam deep in her eyes."
    chizu "Rest here while I go find someone to help."
    rino "But the meeting—"
    chizu "That's..."
    "Her expression shifts, brows drawing together as she chews on her lip."
    rino "(The suppressants won't work.)"
    "My eyes sting, and the tears spill. My chest aches."
    "I haven't had another off-cycle heat since I first met the editor-in-chief, and back then the medicine was useless."
    rino "Haah, aah..."
    "I lift my blouse and squeeze my breasts, digging my fingers in. It hurts, but the pain feels good, and my hips buck."
    chizu "What are you doing?"
    rino "Don't look."
    "Liquid floods my panties, and my mouth hangs slack."
    rino "(If I can just take care of this myself...)"
    "If I can get myself off, my heat should abate. I push my skirt up my thighs and run a finger over the gusset of my panties."
    rino "Haah. Ngh."
    "My thighs glimmer wetly in the dim light filtering in from the office floor."
    "I shove a finger into my panties and move it furiously, almost clawing my insides, but all it does is hurt and bring more tears."
    rino "I'm so aroused...  So why isn't it doing anything?"
    "Looking down, I see that my hand is trembling. My eyes sting with frustration."
    chizu "Ms. Maiguma..."
    rino "Ah... Boss... I can't do it. I'm sorry..."
    "I can't believe this is happening after she just complimented me. Meanwhile, my boss is simply standing there with her one arm wrapped around herself, regarding me intently."
    rino "(Is she mad at me?)"
    "She's covering her face with her hand, and I can't see her expression. Still, her fingers are trembling, and I can hear her panting."
    chizu "Where are your suppressant pills?"
    rino "Huh?"
    chizu "You have them, don't you? I know you want to regain control in time for the meeting, so hurry up and take one."
    "There's a smoldering heat in her eyes as she looks down at me, and I shudder beneath it. My gaze drops to my card holder."
    chizu "...Give me that."
    "My boss grabs the lanyard from around my neck and takes the pills out from the holder."
    "She takes one between her fingertips and holds it out in front of me. I'm entranced by her long, neat, almond-shaped nails, gleaming pink."
    chizu "Take this."
    rino "...Okay."
    chizu "That's right. Good girl."
    "Sticking out my tongue, I take her fingertips into my mouth. The pill slides down my throat."
    "I swallow then cough at the foreign sensation."
    rino "Ah, haah... *cough*"
    "My boss attempts to pull her fingers back, but I clamp my lips around them."
    chizu "Come on, no messing around."
    rino "(Her fingers taste sweet.)"
    "I swirl my tongue around her fingers and trace the tip over her dainty joints. The sweet taste of her skin is intoxicating, and have to force my eyes to stay open."
    chizu "Haah. Mmph."
    rino "Boss?"
    "I let out a heated sigh as she leans in like she's about to kiss me."
    "Her hair tickles my neck, and I squirm."
    "But then she abruptly pulls back, like a magnet repelled."
    chizu "I'm sorry..."
    rino "Huh?"
    chizu "There's no point in the pills, or in masturbating."
    rino "Wha...?"
    "She looks pained as she presses a palm to her sweaty forehead. A bead trails down her temple."
    chizu "If you keep trying, you'll only hurt yourself."
    "Her clear voice trembles as she tentatively draws closer to me again. I can smell her sweat, mingled with foundation and powder."
    "She grabs my hand where it's still buried in my sticky panties, drawing it out then gently squeezing it."
    chizu "So stop."
    "Her hand feels wonderfully cool on mine. My painted nails are sharp, and I relax my hand so as not to dig them into her delicate skin."
    rino "Then you touch me instead."
    "The office chair squeaks. My voice comes out pleading, and the hand on mine twitches with surprise."
    "My heart continues to thud painfully, my heat showing no sign of abating."
    "This is all her fault."
    rino "(Because she was so nice to me. Because she gave me butterflies.)"
    "The burning in my chest, the difficulty breathing... It's all her fault. And on top of all that, I can't stop crying."
    rino "(I can't let this ruin everything, not after how hard I worked for it.)"
    "Memories of last night return, and my chest constricts even tighter. The other team members will be arriving at the office any moment now."
    "I worked so hard, but what will they think if they see me in heat? Imagining it makes the tears come harder."
    
    
    
    
    
    #h scene 2
    chizu "...I'm responsible for this."
    "Her voice whispers in my ear and resonates inside me as my boss sliders herself inbetween my parted legs."

    if patch == False:
        chizu "Wear this."
        "She drapes her blazer over my bare neck."
        "Then she strokes my cheek before reaching down to undo my bra. Her gentle fingers dance over my skin."
        "I fight back the high-pitched moan that tries to escape me."
        rino "Ah..."
        chizu "Bear with it a little longer."
        "I screw my eyes shut and cling to the woman before me, completely at her mercy"
        "My eyelids flicker open as her tongue trails down my abdomen."
        
        rino "(She's so cute.)"
        "I don't know why that thought comes to me as I trail a finger over the red shell of her ear. She twitches and looks up at me."
        "Her expression is so adorable, I feel my stomach somersault."
        "The squeak of the chair and my breathy moans echo through the meeting room as the editor-in-chief caresses me with her tongue until I climax."
        rino "Ah, haah, ah."
        "My body goes limp, and I slump forward. As I cling to my boss, I smell the gentle, fresh scent of mint."
    else:
        chizu "Wear this."
        "She drapes her blazer over my bare neck."
        "Then she stroker my cheek before reaching down to undo my bra. Her gentle fingers dance over my skin."
        "I fight back the high-pitched moan that tries to escape me."
        rino "Ah..."
        chizu "Bear with it a little longer."
        "Her fingers slide up my thighs then slowly undo my skirt. Once it's dropped to the floor, she moves on to my underwear."
        rino "Mm..."
        "I moan, and she looks up at me. When our eyes meet, her deep blue irises shimmer, her painted lips trembling slightly."
        rino "(Here come the butterflies.)"
        "My heartbeat and breathing speed up, and I reach out a hand. When I put it to her neck, her eyes widen and she bites down on her lip."
        rino "(I wish she'd smile at me like she did earlier.)"
        "She turns her gaze away and pulls my panties down before picking up my skirt and carefully placing both articles of clothing on a chair. Then she kneels down before me."
        rino "Ngh. Boss...?"
        "She wraps her hands around my thighs and presses a kiss to the soft inner flesh."
        rino "(Ah. She's serious about getting me off.)"
        "I meet her gaze again, and the heat in them makes me moan. Her eyes shine like a beast's through the dimness of the room."
        chizu "Mmph."
        rino "Ah! Ngh, ah... Boss..."
        chizu "Mm, haah."
        "She teasingly traces my lower lips, avoiding my slit, and my hips buck. She pins me in place and kisses beneath my belly button."
        rino "Mmph, mm. Ngh, yes, right there."
        chizu "Mmph, haah... Maiguma..."
        "I tense my thighs and bury my hands in her long, dark hair. My boss guides one of my legs up to rest on her shoulder, and then she leans in toward my glistening folds."
        rino "Ah! Ngh, ah, haah... So hot... Ah."
        "She takes my clit between her lips and teases the head with the tip of her tongue. The jolt of pleasure makes my stomach clench."
        "My hips spasm, and there's a wet noise as I press up against her face."
        rino "(Her tongue's so soft and wet. It feels so good!)"
        chizu "Hamph. Stop wriggling."
        rino "Hngh, ngh. Ah... Yes, there! That's it, ah."
        chizu "Mm... Hah. I know. I won't stop."
        "My mind starts to grow hazy as wet sounds echo around the room. There's a burning heat deep in my stomach, and I cling desperately to my boss as I try to keep still."
        rino "(She's so cute.)"
        "I don't know why that thought comes to me as I trail a finger over the red shell of her ear. She twitches and looks up at me."
        "Her expression is so adorable, I feel my stomach somersault."
        "But the next instant, all thoughts are erased from my mind."
        chizu "Aah! Ngh, mm, yes, nhaah!"
        "She plunges her tongue inside me, and I can't help but push my hips forward, seeking more of the incredible sensation."
        "When I look down, my brain nearly short circuits at the sight of my boss with her face between my legs, tongue buried within me."
        rino "Aah, ngh... Ah, Boss!"
        "Her tongue hits my sweet spot, and I feel like I'm about to lose it."
        "I move my hips in time with her motions until I feel something hot welling up inside me, then abruptly spill over."
        chizu "Haah, mmph."
        rino "Ah, haah, aah..."
        "My body goes limp, and I slump forward. As I cling to my boss, I smell the gentle, fresh scent of mint."

    chizu "The meeting will start as planned. Join us once you've calmed down."
    "My boss puts her arms around me and whispers into my ear."
    chizu "I'll make sure no one comes in here."
    "Her hard tone cuts through the fuzz in my head, and my heart aches. The cold air chills my skin as she takes her jacket from around my shoulders."
    rino "Um, Boss..."
    chizu "Hm?"
    "I trail off. She takes my lanyard from the table and hangs it around my neck. Then she smooths down her wrinkled clothes and sighs."
    rino "Thank you."
    "My eyes feel crusty with dried tears. When I look up at her, my boss smooths my disheveled hair back."
    "Then she lowers her gaze, gently biting down on her lip. Her brows furrow, and she gives me a conflicted smile."
    chizu "I would've liked to keep going."
    rino "Huh?"
    "But then she frowns, and her tone returns to its usual coolness."
    chizu "Let me know if you're not coping well. A manager is responsible for keeping an eye on their employees' health, after all."
    rino "...Okay."
    "The editor-in-chief nods then leaves the meeting room. I watch her go then wipe my hands across my eyes, scrubbing away the dried tears."

    ###

    "The public bus slows as it weaves its way through the traffic on the big road then comes to a halt at the bus stop. The photographer clicks the shutter to capture it."
    "Many of the people who step off the bus are in pairs, likely here for sightseeing; most are dressed casually and only a few have suitcases."
    
    
    
    
    
    rino "(The article might resonate with these kinds of people.)"
    "I look up at the poster on the bus shelter. Then I call out to the writer who's accompanying me on this trip."
    rino "Um, do you think this route map is a little hard to decipher? A bunch of different buses stop here, so people might get confused."
    writer "Good point. Shall I add that to the article?"
    rino "Yes, please!"
    "The writer quickly snaps a photo of the bus stop with their tablet then jots down a note."
    "I check the time on my phone and relax slightly."
    rino "(Good, we're on track to visit the shopping street in decent time.)"
    "My pitch at the planning meeting was unanimously accepted, and I've been charged with researching and creating it."
    rino "(I do have support, but it's still hard doing it all myself.)"
    "Overjoyed that my pitch had been accepted, I dove head-first into the preparations, and accordingly there's been no major issues so far. Still..."
    rino "(This is my first business trip, so I'm obviously nervous.)"
    "I tuck my highlighted locks behind my ears. I've just had my eyelashes done at the salon, and they flutter ticklishly in the breeze."
    "I set my lips, painted in an ombre look with two new autumn shades, in a determined line and swallow hard."
    rino "(On top of that, there's the worry that I could go into heat at any moment.)"
    "But most of all..."
    
    
    
    
    
    "I glance to the side, and my heart thuds at the sight of her serious, composed profile."
    
    
    
    
    
    rino "(She must've come out of concern for me.)"
    "My field trip happened to overlap with a business trip my boss was taking to our Kanzawa branch, and so she elected to join me."
    rino "(She's been avoiding me less after what happened the other day.)"
    "As I stare at her lips, she traces a finger over them then flicks her tongue out to wet them."
    "I quickly look down so she won't see my face flush scarlet."
    rino "(Crap. Just thinking back on it could send me into heat again.)"
    chizu "Ms. Maiguma."
    rino "Uh, yes?!"
    "I've just got control over my breathing when the sudden sound of my name makes me jump. When I turn to her, she's looking in the opposite direction."
    chizu "It looks like the photographer's only taking pictures of the teahouses."
    rino "Oh, you're right."
    chizu "I'm not sure those kind of standard scenery shots will be a good fit for the article."
    "Looking over, I see that the photographer is indeed focused on shooting the famous geisha district with its distinctive row of teahouses."
    "That would be fine for a general article on the area, but our theme of chance meetings calls for something a little different."
    rino "Right! I'll go talk to him."
    
    
    
    
    
    rino "Um, excuse me."
    "The photographer stops shooting and looks back at me."
    rino "If possible, could I ask you to photograph something other than the tea district?"
    photographer "Like what? We don't have a model... Would you like shots of the river?"
    rino "No, I don't mean of the scenery... I mean like, objects or things that might leave a a lasting impression on someone..."
    "I do my best to explain, but the photographer just looks confused."
    "I look around to see if there's any concrete example I can point to, but nothing jumps out at me. An awkward silence stretches out."
    chizu "Since the theme of the article is chance encounters, I feel like we should have images of things you happen to come across by chance."
    rino "By chance...?"
    chizu "Something like a view of the sunset, which changes with the season, or a piece of folk craft found by the roadside..."
    "My boss's expression softens as she gives me an encouraging look."
    rino "Right, that's exactly what I'd like you to focus on!"
    photographer "...So you'd rather I didn't focus on standard promo shots?"
    rino "Right! I'm thinking we want pictures that'll look good as a thumbnail...!"
    "The vague outlines of the image I had in my head have solidified thanks to the input from the editor-in-chief."
    "The photographer is nodding like he's now got a clear picture of what we're looking for."
    chizu "I think we can leave the exact shots to you. I'm sure you have a better eye for things than we do."
    "I look to the photographer, signaling my approval. I was thinking I had to issue every instruction myself, but my boss is totally right."
    rino "Yes. We want to convey they history of the area, and like a kind of nostalgic, retro vibe... Does that make sense?"
    photographer "Sure thing. Leave it to me."
    rino "Thank you!"
    photographer "Okay, I'll need to find somewhere where the natural light isn't too bright. I'll go take a look around."
    "Smiling, the photographer adjusts his grip on his camera then marches off down the street."
    
    
    
    
    
    rino "Thank you so much. If you hadn't pointed it out, I would've been in a real pickle when I got the photos back."
    chizu "I'm sure you would've managed."
    "She stares after the retreating photographer. He's reconvened with the writer, and they seem to be discussing the shoot."
    chizu "Now you just need to keep an eye on the time so we're not late to the next place."
    rino "It does seem like he's gonna be getting snap-happy now."
    "I cover my mouth as I chuckle. Stealing a glance at my boss, I find her smiling softly, an expression quite unlike the coldness she usually shows me."
    "My throat burns, and there's a pressure in my lungs. I press a hand to my chest and let out a slow breath."
    writer "Sorry to interrupt. Can I check something with you?"
    rino "Oh, yes, of course!"
    "I spin around then hurry over to the writer."
    "I walk as fast as I can in an attempt to shake off something that's not just heat, but a warmth that reminds me of her fingers brushing over my cheek."

    ###

    rino "Thanks so much for your hard work!"
    "I bow my head low, and the photographer nods from the driver's seat of his van."
    "The writer smiles easily at me from the passenger seat."
    rino "Phew..."
    "A wave of relief washes over me, and I readjust my heavy bag on my shoulder. In the distance, I hear the cry of a bird."
    chizu "Good work today."
    rino "Thank you for your help, Boss."
    "The editor-in-chief ended up staying with me all day, fielding calls and emails on her phone while I worked."
    chizu "Well, I'll be at the branch office for the next few days."
    "She's about to turn away, but I find my body moving of its own accord; I reach out and grab her hand."
    chizu "Huh?"
    "Taken aback by my own actions, I freeze. My boss stops in her tracks, her eyes wide with surprise."
    rino "(We were together all day and I didn't go into heat, so it's probably okay.)"
    "On a normal pattern, heats usually occur once every three months, so I'm not due another one yet."
    "Making these internal excuses to myself, I look down, still clasping her hand."
    rino "Since we're here, would you like to come to the shrine with me?"
    chizu "To the shrine?"
    rino "The company booked us into the same hotel, so we can head back together afterwards."
    rino "I want to, you know, pray for the article's success, or something like that!"
    "This is hard for me. But my heart is racing, and I don't want to let go of her hand."
    "I glance up to check her expression, but she looks away, chewing on her lower lip."
    chizu "Sure."
    "With that, she sets off walking."
    "Holding back the grin that threatens to break across my face, I follow after her, my boots ringing out across the paving stones."
    
    
    
    
    
    rino "(Everyone around here seems to be in a couple.)"
    "I look around as we walk up the path to the shrine."
    "Raising my eyes to the sky, I see the evening light filtering in between the torii gates leading up the path. A breeze rustles the leaves of the hinoki cypress trees."
    "Two women who appear to be a couple are drawing fortunes. Beside them, a smiling man and woman are showing one another what they got."
    "I don't know whether they're Alphas or Omegas, but I can't help but smile at the heartwarming sight."
    rino "(When I was little, I wanted that for myself, too.)"
    
    
    
    
    
    "I steal a glance beside me. Her dark hair flutters in the wind, bringing with it the scent of mint."
    "My boss must like perfume, as she's always wearing the same scent. Though when I go into heat, I barely register it."
    rino "(She's so pretty.)"
    "The shimmery dusting of highlighter on her cheeks catches the light, making them glow; the line of her jaw is sensual, her skin dewy."
    "I'm staring at her, entranced, when she suddenly opens her mouth to speak."
    chizu "You're from around here, aren't you?"
    rino "Huh? Oh, yes, I am."
    "Wondering whether she caught me staring, I quickly turn my face forward and start to walk again."
    "I surreptitiously take a deep breath and force myself to focus on the conversation."
    
    
    
    
    
    rino "But I lived closer to the sea. I used to work in the transportation planning department at the local town hall."
    "Local government is happy to employ Omegas, and I started there straight out of high school, commuting from my family home."
    "My coworkers were really nice, and I enjoyed the job, but in the end I overcame my parents' opposition and moved to Tokyo."
    chizu "You pitched the sight-seeing buses scheme, right?"
    rino "Oh, you know about that?"
    chizu "You interviewed with the deputy editor-in-chief, but she filled me in. Said that you're good at clerical work and have a proven track record of pitching new projects."
    "It makes sense that, being the methodical person that she is, she would've asked for info on the new recruit."
    chizu "So I was curious to see what kind of person you'd be."
    rino "Really?"
    chizu "Since most of our team are people are who've transferred in from other editorial or sales teams, it was nice to have a fresh face."
    "She tucks her hair behind her ear then reaches for the ladle at the cleansing station. Holding her handkerchief between her lips, she pours water over each hand then dries them."
    "I follow suit. As I muse on her words, I feel a lightness inside, and my lips curve into a smile."
    rino "(She was interested in me as a person, regardless of being an Omega.)"
    "My boss takes out her wallet and picks out some coins for an offering, then gives some to me."
    rino "Wouldn't one coin be enough?"
    chizu "People say that is love's lucky number."
    "Counting the coins in my hand, I see that they total yen."
    rino "Pfft. Seriously?"
    chizu "It's a common saying. Huh? You've never heard it?"
    rino "No, I have..."
    "She's usually so serious and uptight, I can't help but giggle. I have no idea why she thinks I need luck in love, but it's sweet of her."
    "We face the inner shrine and perform the prayer. When we're done, I buy a charm as a present for Honami, and then we start making our way back."
    "Just then I spot a little path leading off from the main one."
    rino "Awh, they didn't have these cute ema tablets when I was a kid. These are the ones for matchmaking!"
    "I rush over to look at the little votive  tablets hanging on the wall. Some of them are heart shaped or decorated with images of happy couples."
    chizu "You've been here before?"
    rino "Yeah, I came here a lot with my parents when I was little."
    rino "When I was older, I wanted to come here on my own."
    "I run my hand over the tablets on offer. I pick up one of the designs I remember from my childhood—a white horse adorning the plain wood—and drop my money into the box."
    rino "Are you going to write one?"
    chizu "I'm good. I'll just watch you do it."
    "She comes in close to me, picks up a marker pen, and holds it out to me. I take it and place the tablet on the writing table."
    rino "But my parents wouldn't let me. Said it was dangerous for an Omega to wander around alone when there aren't many people around."
    "I had much more freedom when I was young, but as soon as I hit puberty and got my first heat, my worried parents and friends put a stop to that."
    "I didn't feel isolated or anything, but I always longed for the freedom to go where I pleased."
    rino "So traveling was always my dream."
    chizu "Your dream, huh?"
    "After moving to Tokyo, I'm now working in the tourism industry and living alone, albeit in an apartment with a lot of security. It's the life I've always dreamed of."
    "The editor-in-chief's composed expression shifts slightly, and she lowers her gaze."
    "Sighing, I pull the cap off the marker pen."
    rino "But I suppose as an Alpha, you wouldn't really understand."
    "Embarrassed at myself for rambling, I focus on the ema, writing my name and the date in the bottom right corner."
    
    
    
    
    
    chizu "Maybe I didn't have the same experience as you."
    "My boss responds in a soft tone. I turn back to her to find her gazing at the wall of tablets."
    chizu "But I was never able to travel much, either."
    rino "Really? Even as an Alpha?"
    chizu "My father died when I was young, and my mother buried herself in her work, I suppose because she'd lost her destined mate..."
    rino "(Her destined mate? That means...)"
    "Her parents were an Alpha and an Omega, though I don't know which was which. My boss's expression is shadowed with longing and regret."
    chizu "We only went on one family trip, while my father was still alive."
    rino "Oh, I see..."
    chizu "So I think I dreamed of it, too, same as you."
    "She smiles awkwardly, and my stomach flip-flops. I press my hand to my chest; my heart slows, but my cheeks still burn."
    rino "I had no idea..."
    rino "(I thought I was getting my heat there for a second.)"
    "But this is different to being in heat. I don't know what to do about my racing heart, so I close my eyes and take a breath."
    "I focus back on the tablet and scribble my wish on it: I wish for the editorial team to be happy, healthy, and to thrive at work."
    "My wish is probably at odds with all the other romance-related ones, but never mind. I put the lid back on the pen and return it to the pen holder."
    
    
    
    
    
    "I walk along the rows of tablets tied to the vermilion fences that line the path, searching for a gap."
    "As my gaze trails over sweet messages to loved ones and wishes for roamnce, one in particular catches my notice."
    rino "I wish to find my destined mate...?"
    "I can't help but smile at those words, clearly written by an Omega."
    "It's sweet that they're still honestly hoping for a miracle."
    rino "(In a sense, maybe it's good to be open about what you want.)"
    "There's a lot to dislike about living a life dictated by your desires, but maybe it's not all bad."
    rino "Must be nice, actually."
    "Noticing my smile, the editor-in-chief stops and runs her eyes over the rows of tablets. But in contrast to me, she frowns and chews on her lip."
    chizu "Ngh..."
    rino "Is something wrong?"
    chizu "Do you ever think about meeting your destined mate?"
    rino "Uh, it seems pretty unrealistic, so I've never really thought about it."
    "There are reality shows about fated pairs, but most of it is as fictionalized as the many TV shows and novels on the topic."
    "Yet my boss looks serious, her eyes lowered."
    rino "Call it instinct or the whims of the gods, I don't care—I just know that I want to be with someone I truly love."
    "With that declaration, I slide my ema into a gap beside the one I was just reading. I connect the threads and tie them off tightly."
    rino "(Why would she ask me that?)"
    "In all honestly, I don't want to meet my destined mate."
    "I mean, I..."
    "I leave the tablet where I've hung it and readjust my bag. A gust of wind blows down the small path, shaking the trees."
    rino "Why aren't you saying anything?"
    "But she simply averts her eyes, still chewing her lip."
    "I see her dry lips tremble, the lipstick smearing."
    chizu "I'm sorry."
    rino "Wait, do you think that we—"
    "My breath catches in my throat, and my head throbs. When I grab her hand, her fingers are as cold as ice."
    "I look up into her face, but she shuts her eyes and turns her head away."
    rino "(Why...?)"
    "I wouldn't usually go into heat simply from being in contact with an Alpha."
    "But for some reason, it happens whenever I get close to her."
    "My brain is on fire. My boss's pretty face contorts as she tries to pull away from me."
    rino "Look at me. I have my heat suppressant."
    "My mouth is dry, and my eyes prickle. Why won't she look at me?"
    chizu "The pills don't work...!"
    rino "Don't say that."
    "I want to tell her that we don't know that without testing it, but then I recall a dry sensation on my tongue."
    rino "(We already tested it, that one time...)"
    chizu "It seems like you were unaware. But you should know that, once in rut, an Alpha will claim their mate by force."
    chizu "Regardless of what you might want. So get away from me."
    "With her eyes screwed shut, she tries to shake off my hand and pull away from me, but her protests are devoid of her usual strength."
    rino "(So these feelings I've been having are...)"
    "The tightness in my chest, the urge to cry, the joy of being beside her... Those were all simply instinct determined by my DNA?"
    rino "It's not true...!"
    "I reach out and touch her cheek, turning her head to face me."
    
    
    
    
    
    chizu "Mm..."
    rino "Nhaah."
    "I lean in, and my lips just barely graze hers. She opens her eyes, and our gazes meet."
    rino "Ngh, ahngh..."
    "Her eyes are a deep blue, glowing like smoldering embers."
    "The scent of mint emanating from her neck slides down my throat, stirring a fire in my belly and making my vision waver."
    "The heat is almost painful, blazing hotter in time with my pounding pulse."
    rino "Ah, mm, haah. So hot."
    
    
    
    
    
    "My knees buckle, and pain shoots through them as they hit the cold stone floor."
    "One of my boss's hands is at my elbow, keeping me from fully collapsing, and I end up slumped against her."
    rino "Don't touch me!"
    "She freezes at my shout. Her eyes flicker like candlelight."
    "I pull back and ball my hands into fists, fighting to gain control of myself. My nails bite into my palms, the pain anchoring me."
    "Then I grab my fallen bag, sling it over my shoulder, and run."
    chizu "Ms. Maiguma...!"
    "In the distance, I can hear her calling to me. But I keep running, desperate to shake off that scent, until I'm out of breath."

    ###

    rino "Mmph... Ngh."
    "The stark white sheets are soft against my skin as I curl into a ball. Tears spill from my eyes, tracking my eyeliner down my face."
    "My hand covers my mouth, the moans escaping from it so wanton I can hardly believe they're coming from me."
    rino "(It's so intense... But is it all because she's my destined mate?)"
    "The warm fuzzy feelings whenever I noticed little things about her, saw the kindness in that pretty face... I'd thought all those feelings were my own."
    "But it was all simply biological instinct determined by my DNA. That truth makes my heart ache, yet I continue to moan desperately."
    rino "Haah!"
    "I clamp my right hand between my thighs and press down against my stomach. My hips buck up weakly to meet it."
    "There's a wet, slippery sound as my thighs rub together. Biting down on my finger, I screw my eyes shut."
    "Recalling the gentle touch of her fingers, I slide my hand down my stomach."
    rino "(No... She wasn't rough like this.)"
    "The images playing behind my eyelids are dim and hazy. I can't recreate her breathy moans or the coolness of her fingertips."
    rino "Boss..."
    "Though I bury my face is in the starchy white hotel pillow, all I can smell is my own shampoo and the scent of my heat."
    "I run a finger over my lips, hoping to find a lingering trace of her scent. My lipstick smears, and I catch the faint, frosty smell of the winter air."
    rino "Yes, right there..."
    "The words spill from my lips. I screw my eyes shut, trying to follow the scent, acquiescing to my desire and pressing my hand over my shorts."
    rino "Chizu..."
    "The first time I heard it, I thought it was such a pretty name. I imagined the kind of amazing person it might belong to."
    "My cheeks burn with emotion and desire. I gasp as my stomach clenches deep inside."
    "My womb is crying out for the DNA of an Alpha... of my destined mate. I'm at a loss for what to do as the thought sends more tears coursing down my cheeks."
    rino "Aah... Chizu!"
    "My hips press up against my hand while I trace my lips with the other. As I desperately moan her name, the heat building within me spills over."
    rino "Ngh, ah... Chizu..."
    rino "Love you..."
    "Abruptly, my hand stills. The words are out there now, echoing in the dim room, and I can't take them back."

    if patch == False:
        "*knock knock*"
        "My head jerks up at a light knock on the door. Putting one hand to my pounding head, I brace myself on the bedside table with the other and push myself up."
        "I fumble to straighten my clothes. I don't have the energy to search for my key card."
        rino "Who is it?"
        "Holding my burning stomach, I stumble toward the door, unlock it, and open it a crack. A woman I don't recognize is standing on the other side."
        "The woman holds out a handkerchief to me, putting one finger to her slightly parted lips."
        woman "This is yours."
        rino "Huh?"
        "I glance down at my bag, abandoned right next to the door."
        "Fortunately, I made it into a taxi, but I don't really remember getting to the hotel or finding my room."
        rino "(I must've dropped it on my way.)"
        rino "(Huh? Hang on...)"
        "Just then, a throb of pain lances through my neck, and my heart abruptly starts to pound."
        rino "(She's an Alpha!)"
        "The woman's lips twist slightly. The hot breath that escapes them sends a chill up my spine."
        "The pink handkerchief I dropped is one of my favorites; it must be soaked in the scent of Omega heat. Before I can fully comprehend the situation, a strong Alpha smell hits me."
        
        woman "Haah, mmph, haah."
        rino "Ngh, ah, no!"
        "The woman grabs me by the arm and pushes me back into the room, pinning me against the closet. I grimace as pain shoots up my arm."
        woman "Haah. Your neck... Haah..."
        rino "No...!"
        "Her musky scent makes my head spin. She's entraptured by my pheromones, all logic and reason deserting her; her pupils are blown large, her brow furrowed."
        rino "Stop... What are you doing?!"
        "I desperately try to shake her off, but I'm no match for an Alpha's strength. Driven by instinct, her mouth closes in on my neck."
        "The hard enamel of her teeth grazes my skin. My arms are pinned in place, and my head is on fire."
        rino "(No, no! I don't want this!)"
        "When I close my eyes, my boss's voice comes back to me."        
    else:
        chizu "Boss... Ngh, haah..."
        "I squeeze my arms against breasts, remembering the tip of her tongue tracing them the day we first met."
        chizu "Ahn..."
        "The thick fabric of my bra pushes back against my nipples. Everything feels so good as I rub myself against the bed."
        "My fingers, supposed to be keeping me quiet, trace my lips then slip into my mouth."
        chizu "Nngh... Ah!"
        "I slide my middle finger further in, pushing down on my tongue, and the pressure makes me moan."
        rino "(No... She wasn't rough like this.)"
        "The images playing behind my eyelids are dim and hazy. I can't recreate her breathy moans or the coolness of her fingertips."
        chizu "Boss..."
        "Though I bury my face in the starchy white hotel pillow, all I can smell is my own shampoo and the scent of my heat."
        "I run a finger over my lips, hoping to find a lingering trace of her scent. My lipstick smears, and I catch the faint, frosty smell of the winter air."
        chizu "Yes, right there..."
        "The words spill from my lips. I screw my eyes shut, trying to follow the scent, acquiescing to my desire and pressing my hand over my shorts."
        chizu "Chizu..."
        "The first time I heard it, I thought it was such a pretty name. I imagined the kind of amazing person it might belong to."
        "My cheeks burn with emotion and desire. I gasp as my stomach clenches deep inside."
        "My womb is crying out for the DNA of an Alpha... of my destined mate. I'm at a loss for what to do as the thought sends more tears coursing down my cheeks."
        chizu "Aah... Chizu!"
        "My hips press up against my hand while I trace my lips with the other."
        chizu "Haah, nhaah! Aah... Chizu! Yes, there!"
        "As I desperately moan her name, the heat building within me spills over."
        chizu "Ngh, ah... Chizu..."
        chizu "Love you..."
        "Abruptly, my hand stills. The words are out there now, echoing in the dim room, and I can't take them back."
        "My inner walls quiver, aching for fingers to fill them, and I let out a long breath as my panties flood with liquid."

    chizu "...I'm responsible for this."
    chizu "Bear with it a little longer."

    "The gentleness of the tone and the heat behind those cold words cuts through my instinct. I tense my body, fighting to tear the gap wider."
    "I squeeze my fists so tightly that my nails cut into my palms, then I brandish my hands with all my might."
    rino "I said no!"
    "One of my fists slams into the woman's shoulder. As she stumbles from the impact, I grit my teeth and push with my shoulder, shoving her away from me."
    
    
    
    
    
    "I rush out of the room just as someone is coming out of another one, and I crash into them."
    rino "Ngh! Ow..."
    "My head slams into something hard, and I reflexively reach up to rub it; but as I look up and meet the person's eyes, my hand stills in mid air."
    rino "Chizu...?"
    chizu "What do you think you're doing with my employee?"
    "With one arm wrapped around me, she reaches out with her other hand to grab the woman's wrist and addresses her in a cold tone."
    "The woman seems to have snapped back to her senses, and her face pales as she looks up at Chizu."
    
    
    
    
    
    chizu "You know it's a crime to claim an Omega against their will, yes?"
    "I've never heard such anger from her before. The woman mutters a dazed apology."
    rino "Um, I..."
    "My brain still isn't working properly. Chizu tightens her arm around my shoulders, putting herself between me and the other woman."
    chizu "Sorry I didn't get here earlier."
    "The Alpha scent emanating from her neck makes my head throb. Her tone is harsh, yet it still makes my knees go weak, and I lean in to her."
    rino "(She's sweating.)"
    rino "(Right, she must've come back to her room.)"
    "She was there, just meters away from me as I consoled myself... Heat blossoms in my belly at the image."
    chizu "Haah. I'll sort this out. If you're in a fit state, could you come with us to the front desk?"
    "Her hot breath brushes my ear, and a shudder of pleasure runs down my spine. I struggle to force words out as my mind goes hazy."
    rino "I can't..."
    rino "I don't want to fight it any longer."
    chizu "Ms. Maiguma...?"
    "I snuggle up against her, and her shoulders quake slightly."
    rino "I don't want you to leave right now. Please, help me."
    "I know I'm acting like a petulant child as I bring my lips to her neck. Chizu moans slightly, then her brows furrow and she looks down."
    "After she's regained her composure, she looks back up at the woman."
    chizu "Do you have any ID on you?"
    "The woman nods then pulls a card case from her bag and shows it to Chizu."
    "Chizu snaps a photo of it then goes on flatly."
    chizu "I'll send the police your way tomorrow morning. Right now, I'm going to report this to the front desk. Could you come with me?"
    "With that, she pulls away from me, her hand still wrapped around the woman's wrist. She takes a key card from her bag and hands it to me."
    chizu "My room's just over there. You're welcome to use it."
    
    
    
    
    
    "She probably doesn't want anyone going into my room until the police get here."
    "But right now, her kindness is making my chest ache and bringing tears to my eyes. I take the card from her."
    "I head two doors down and slide the card into the reader."
    "Before I step into the room, I glance toward the elevator to see Chizu leading the woman toward the lobby. Our eyes meet."
    rino "(I should be able to handle myself better than this...)"
    "Spurred on by her concerned look, I go into the room and close and lock the door. Then I lean back against it and let out a deep sigh."

    rino "Fwaah... Haah."
    "Blowing out a deep breath, I rest my hand against the wall of the shower cubicle."
    "The water cascades over me like cool rain, calming my flushed skin. My heartbeat slows, though it still thuds loudly."
    "I return the shower head to its holder then glance at the tiny shampoo bottles lined up neatly on the little shelf."
    rino "(She's so particular.)"
    "Each travel bottle is labeled in Chizu's neat handwriting. I smile to myself."
    "Since she's staying for several nights, she's declined the housekeeping service, but the room is still perfectly clean."
    rino "(I can still smell her.)"
    "I wring out my hair then quickly wipe myself off with a towel so that her scent doesn't bring my heat back."
    "Although I can often calm my heat by taking care of myself and cooling off, today the mere sensation of the towel across my skin makes me quiver."
    rino "My skin's so hot..."
    "I'm overcome with the urge to slide my hand between my legs, and I bite down on my lip to suppress the instinct."
    rino "No touching..."
    "After all, if it's not Chizu's hands on me, it's not going to make any difference."
    
    
    
    
    
    "I tie my gown tightly then leave the bathroom. The moment I step into the room, her scent hits me; my head spins, and I wrap my arms around myself."
    rino "Haah, mmph."
    "I'm leaning against the wall to compose myself when the doorbell chimes. I shudder as I recall the earlier incident, but then I hear a gentle voice through the door."
    chizu "Ms. Maiguma? It's me. I'm all done..."
    "I unlock and open the door before she can finish. Cool air and Chizu's scent wash over me as Chizu stands there, her brow furrowed with concern."
    chizu "I see you took a shower."
    rino "I thought it might calm my heat."
    chizu "Oh."
    "She looks away from me and walks into the room, telling me not to lock the door."
    "She goes over to the desk and sits down, opens her laptop, and calls up her email software."
    chizu "The police will come by tomorrow to take a statement. You'll need to leave your room as it is for now."
    "She glances back at me and frowns, pushing her hair back behind her ear."
    chizu "There's some unopened jasmine tea in the fridge. Let me know if you want to order room service."
    rino "Uh, okay."
    "She nods, businesslike, and I clutch the hem of my robe. As she starts to clack away at the keyboard, I slump down onto the bed."
    "I steal a glance at Chizu, her profile illuminated by the soft hotel lighting and the glow of her screen."
    chizu "Nngh."
    rino "(It seems like she's struggling.)"
    "Her cheeks are flushed, her pupils blown wide, and her fingertips slam against the keys harder than usual."
    rino "(Has she been holding herself in check all this time?)"
    "Though I don't know how Alphas experience it, I know what it's like to feel a frustrating burning in my stomach that just won't abate."
    "If she's going through the same thing, then it must be just as hard, or even worse, for her."
    rino "(Now that I think about it, she's always avoided looking at my neck.)"
    "Pressing my hand to my neck, I sigh breathily. If Chizu is my destined mate, her feelings must be even stronger than those of the woman who just tried to forcefully claim me."
    "But even now, Chizu is fighting with herself to suppress her primal urges. The thought makes my heart clench painfully, and I open my mouth without thinking."
    rino "Why won't you help me out like you usually do?"
    "The clicking of the keys pauses for a moment, but then she looks back at the screen and continues typing."
    chizu "I'm the same as that Alpha who assaulted you."
    rino "Huh?"
    chizu "I touched you while pretending I wasn't filled with the desire to claim you. That was wrong of me."
    rino "No, don't say that! I'm the one who wanted it."
    "Her brows knit together and her eyes shimmer with regret. I hold her gaze as I continue to speak."
    rino "And you did it for my sake."
    chizu "You wanted it because I'm your destined mate. You simply let me get away with it."
    rino "No, that's not..."
    "Her words sound pre-prepared. I stand up, my head buzzing. But Chizu goes on in a gentle tone, like she's persuading a small child."
    chizu "I'll have someone else take over my role at work. Don't worry—I'll make sure this doesn't count against you in any way."
    rino "What are you trying to say?"
    chizu "I should've done this from the start. I'm truly sorry."
    "Chizu looks up at me. Even as she forces her lips into a smile, tears bloom in her eyes."
    "I see myself reflected in them. My mouth thins into a line at the look on her face, illuminated by the cold white light of the screen."
    chizu "All this time, I've been taking advantage of the fact that you were unaware. Even though I knew that, as your destined mate, I should've kept my distance."
    rino "But I don't want that."
    "My brain is on fire, and my lungs hurt with every breath. Tears well up in my eyes, dissolving my eyeliner."
    chizu "I'm sure it'll abate if you spend the night here."
    rino "It won't."
    "I know it won't. I want her so badly it hurts."
    "But Chizu turns back to her computer, clearly done with the conversation."
    rino "(Why...?)"
    "My body moves of its own accord as I wedge myself between Chizu and the desk. Then I seize her face between my hands."
    
    
    
    
    
    rino "I don't want you to go! You're MY boss!"
    chizu "Mmph...!"
    rino "So please... look at me."
    rino "Just because we're a fated pair, you think my feelings for you aren't real?"
    "Her blue eyes widen and tears well up in them, falling like water droplets. They trail from the corners of her eyes, warming my palms."
    rino "Even though I care so much for you?"
    rino "I love you. I want to be with you."
    "I keep her face firmly in place, preventing her from looking away; but then I relax my grip, stroking her cheek."
    rino "I want to feel your name on my lips. Every little thing I notice about you makes me so happy."
    chizu "...Ms. Maiguma."
    "Her voice is hoarse, her eyes narrowed. Even now, she doesn't try to shake me off as she sits there, tears trailing down her cheeks."
    rino "(She's adorable. I love her so much.)"
    "I push the words back down my throat then bring my lipsticked lips towards her pale pink ones as though I'm being drawn inexorably toward them."
    chizu "You only feel this way because you're in heat."
    rino "I don't want to hear it."
    chizu "Mm, haah... Wha..."
    rino "Mm... Haah. So cute."
    "Chizu's lips glitter from the gloss I've transferred to them. I flick the tip of my tongue over them, as though to taste the sparkles."
    rino "I love you. And I want you to love me back."
    rino "I want you to tell me I look good when I've done my makeup differently because I knew we'd be working together."
    chizu "Haah, mmph... I understand. Ms. Maiguma, you're..."
    rino "No, you don't... Chizu."
    "I cut her off. As I stare intently into her eyes, she shuts her mouth, flustered."
    chizu "...Rino?"
    rino "Yes."
    "My heart swells with joy as her scent strengthens. My pulse races, but it doesn't hurt this time."
    "I put my arms around her, pulling her close and bringing my lips to her neck."
    chizu "Nhaah, mm."
    rino "Mm, haah."
    "Her hot, damp skin is soft and pliant against my lips. Sucking on it doesn't leave enough of a mark, so I nibble gently instead."
    rino "(Her skin's gone all red.)"
    chizu "Nhaah, mngh."
    rino "Mmph, ah, haah."
    "I kiss and suck at her neck, trying to leave hickeys, then finish with a gentle bite."
    "Red bruises bloom across her pale skin, dotted with the indentations of my teeth, purplish like the prick of thorns."
    rino "Since I'm an Omega, I guess biting isn't going to do much."
    "I soothingly kiss the angry welts."
    "Her clavicle stands out prominently above her decolletage, and she trembles slightly as I brush my lips over it."
    chizu "Haah... But this isn't... going to calm your heat."
    "I wrap my arms tightly around her, and she breathes a deep sigh."
    rino "(That's not why I'm doing this.)"
    "Unable to hold back any longer, Chizu moans and leans into me. I capture her lips with mine and feel her hot, wet tongue slide over them."
    rino "Mm, mmph."
    chizu "Aah, haah, mm."
    "We moan between kisses. When I push my tongue between her lips, she eagerly accepts it. Our saliva mingles, and her moans send tingles to my tummy."
    "Chizu's eyes shimmer, and a tear trails down her cheek. Then she pulls me closer and twines her tongue around mine."
    rino "Ngh, mmph ▼ Chizu, ah... You're so cute."
    chizu "Mm, haah, mmph."
    "When I pull away for a moment, Chizu immediately draws me back toward her."
    "A sweet smell surrounds us, her scent mingling with mine. Fire blazes in my belly."
    "Her body as she clings to me seems smaller and more fragile than usual."
    "I lean my face closer, and I hear her sharp intake of breath."
    chizu "You're so pretty, Rino."
    "Her breath grazes my earlobe, sending a shiver of pleasure down my spine."
    rino "Ah▼"
    "My stomach clenches, and my hips buck. My mind goes hazy as a ragged moan tears from my throat."
    
    
    
    
    
    if patch == False:
        rino "Huh?"
        chizu "Haha, ah, mmph... Has your heat abated, Rino?"
        rino "Uh, yes..."
        "Chizu pulls me close as she catches her breath. The previous melting heat has calmed, and her body now feels pleasantly warm."
        rino "(I came...)"
        "Her sweet moans resonate in my stomach, and then..."
        rino "(Oh my gosh, I'm so embarrassed!)"
        "A wave of embarrassment rushes over me, and I feel my cheeks flush with a different kind of heat. My senses return to me, and my pulse quickens at the feel of Chizu's soft skin."
        "She's cooled off, too, but her arms are still wrapped around me. Does that mean..."
        rino "(Did I get through to her?)"
        rino "Um, Chizu, I... got carried away in the moment, but I  meant what I said—"
        "I want to make sure she's got the message, but Chizu cuts me off, her voice dripping with arousal."
        chizu "Rino. Close your eyes."
        
        "Instinctively, I do as she asks. My lashes are crusty with dried tears, and my eyes sting."
        rino "They're closed..."
        "Chizu takes me by the shoulders and guides me to my feet. Before I can miss the warmth of her body, she pulls me against her."
        chizu "If you look into my eyes, you'll just go into heat again. This way..."
        rino "Eep!"
        chizu "Don't worry, the bed's here."
        "Dim light glows behind my eyelids. I feel the soft mattress at my back as she lays me down."
        "Then Chizu's presence draws away, and I suddenly have a horrible feeling."
        "I see her leaving as soon as the elevator doors open, hear her lingering voice as she leaves me alone in the meeting room, and I'm compelled to speak."
        rino "Chizu, was what I said still not enough for you?"
        rino "I love you. But if you're going to leave me, at least have the decency to tell me to my face."
        rino "Please..."
        "Still, I keep my eyes closed, and they prickle as I imagine her telling me bluntly that this is over—but I have no more tears to shed."
        chizu "You're so predictable."
        "Her warm, exasperated voice floats to my ears along with the quiet noise of rustling fabric."
        "I can't hear anything from outside the hotel room; only the faint sounds of Chizu moving and fabric falling to the floor."
        "The bed shudders, and I feel her close by. I moan when her cold fingertips brush my cheek."
        "She takes hold of my right arm. The bed creaks and the mattress bounces."
        rino "Chizu?"
        chizu "I thought I was the only one suffering. I'm sorry."
        "Her fingers trail down to my wrist, and her cool fingers entwine with my blazing hot digits."
        rino "Mm."
        "She clambers on top of me, and I gasp as her soft skin brushes my thighs."
        chizu "Don't look away from me. If I try to bite you, you run. Can you do that?"
        "She murmurs directly into my ear in a soft, slightly awkward voice, rather than the one that drips with arousal."
        "There's a pleading note to it, and I nod decisively."
        rino "I can."
        "At last, I open my eyes. My vision flashes with blue light."
        
        rino "Haah... Chizu."
        "Her eyes shimmer with suppressed heat. Her hand tightens on mine, and I feel her hot breath on my face as her scent overwhelms me."
        chizu "I won't leave you."
        "The light catches her collarbone peeking out over black lace. Just imagining the feel of her skin makes heat pool in my stomach."
        "Chizu's fingertips dance around my chest, and out of the corner of my eye, I can see my nipples hardening."
        rino "Ngh, ah."
        chizu "I've wanted to do this for so long."
        "She squeezes my hand, using her other to tentatively caress my breast."
        "Her perfectly manicured brows knit together in concentration. Her pale pink lipgloss absorbs the light and shimmers captivatingly."
        rino "Nngh, haah, mm."
        chizu "Mm, haah."
        "She captures my lower lip between hers. Keeping my eyes locked on hers, I hungrily slide my tongue into her mouth."
        rino "Ngh, haah. Chizu!"
        chizu "Haah, mmph."
        "Her hot tongue feels incredible. We kiss until my lungs feel like they're about to burst."
        "Pleasure shudders down my spine as I point my tongue and lap at the underside of hers, trying to find out what makes her tick."
        rino "Mm, haah. I love you."
        chizu "Ngh..."
        rino "How do you feel?"
        chizu "I don't have the same way with words as you do."
        "My heart pounds at the sight of her, so uncertain, and so unlike her calm and collected work demeanor."
        rino "(She's not gonna let go of my hand.)"
        "In place of words, I feel the heat coming from our entwined fingers, and I smile happily."
        rino "Then I want you to show me with your body."
        rino "Nhaah. Until I forget all about fate and destiny and all that crap."
        chizu "You really want me to let loose on you?"
        "As though in response, I feel liquid gushing from between my legs."
        rino "Mm, ahm. Yes."
        chizu "Tell me if it gets too much."
        "I smile to allay her concern."
        rino "I'm not the weak little Omega you seem to think I am."
        chizu "Then I suppose I'm not the big strong Alpha you think I am, either."
        "Her eyes narrow with relief, and then she lowers her face to my chest."
        rino "Ngh, ah."
        "I moan and writhe beneath Chizu's ministrations."
        "Her gaze doesn't break from mine the entire time as she touches all my most sensitive spots in just the way I like."
        "She clasps my hand tightly, conveying her emotions with touch rather than words, while I drown in the ocean of her heat and her scent."
        chizu "Mm. So pretty."
        rino "Haah, mm."
        "Her soft tongue brushes my lips. Saliva trails from the corner of my mouth."
        "My head buzzes and my vision shimmers, but I keep my eyes open, staring into Chizu's deep blue irises."
        chizu "Rino?"
        "A sweet voice filters through the haze in my mind."
        rino "Ngh..."
        "Feeling like she's about to let go of my hand, I tighten my grip."
        rino "Love you... Chizu..."
        chizu "..."
        "A whisper of breath across my ear. I can still feel her warmth through our loosely joined fingers."
        "I smile at the weight pillowed on my chest, and a breathy noise escapes my lips."
        rino "Ngh."
        "The tip of her nose nuzzles my neck. Mingled with her breath is the faint, cool scent of winter."
        chizu "You smell good, Rino."
        "I'm enveloped in her warm skin and soft scent."
        "Drowsiness fills me, and at last I let go of conscious thought and drift into sleep."
    else:
        chizu "Mm, haha, aah. You're adorable, Chizu."
        chizu "Nhaah, mmph, ah! Nngh."
        "With one hand cupping her cheek, I slide the other around her waist then slip it under her dress to touch her hot, sweaty skin."
        chizu "Mm, aah."
        chizu "You have beautiful breasts."
        "Pushing her dress up, I get a view of her underwear, delicately embroidered with little bluebirds. I stare at the mounds of her breasts then slide a hand under the cup."
        "My fingertips brush a hard nub, and I roll my index finger over it."
        chizu "You're in rut, too."
        "Adorable. Her nipples are smaller than mine, but they're seeking the same stimulation."
        "Heart pounding, I pull the cup aside, and my stomach flips at the sight of her hard, pink nipple peeking out."
        chizu "Haah, mmph, aah."
        "I press down on it, feeling her twitch beneath me, her hands clutching at my back."
        rino "(She likes that.)"
        chizu "Mm, ah... Don't do that."
        chizu "What? You don't like having your nipples teased?"
        "I whisper into her ear, enjoying the way she gasps, her lashes trembling over her downturned eyes."
        "I push down on her nipple again, wanting to see more of her rapturous expressions."
        chizu "I'm gonna—ahn! Ah! Nnngh!"
        chizu "Don't hold back."
        "I run my tongue along her earlobe, avoiding the single gold stud."
        chizu "Haah!"
        "She moans deeply and her scent strengthens. Liquid gushes out of her, staining her white panties."
        "My hips move reflexively, grinding against her."
        rino "(No, I don't wanna be the only one getting off!)"
        chizu "Rino...?"
        "I press my lips to hers as though to capture the heat in her voice."
        chizu "Aah, haah, mm."
        "We moan between kisses. When I push my tongue between her lips, she eagerly accepts it. Our saliva mingles, and her moans send tingles to my tummy."
        "Chizu's eyes shimmer, and a tear trails down her cheek. Then she pulls me closer and twines her tongue around mine."
        chizu "Ngh, mmph ▼ Chizu, ah... You're so cute."
        chizu "Mm, haah, mmph."
        "When I pull away for a moment, Chizu immediately draws me back toward her."
        "A sweet smell surrounds us, her scent mingling with mine. Fire blazes in my belly."
        rino "(I'm sure she's feeling the same way.)"
        "I press my hand to her warm stomach and feel the muscles twitch beneath my palm."
        chizu "Haah, mmph."
        "I trail my finger around her bellybutton then slide it down."
        chizu "Nngh!"
        rino "(Not there. A little lower.)"
        chizu "Aah, nhaah!"
        chizu "That's the spot▼"
        "I push my fingers inward, and her hips buck like she's trying to get away. Holding her  still with one hand, I use my left to dig into the same spot."
        chizu "Nhaah, ah... What are you... Ngh, ahn, ah! I'm—!"
        chizu "Feels good right here, doesn't it?"
        "Just beneath the cervix... When I push on her abdomen, I can tell her inner walls are twitching, desperate for my fingers."
        chizu "What are you... Ah! Nngaah!"
        chizu "I learned to do this to get off when I'm in heat but not in a situation where I can touch myself down there."
        "Her moans are breathy and sensuous. Filled with affection for her, I press a kiss to her cheek."
        chizu "I want more. Don't hold back. Come for me."
        "I rock my hips, leaning my weight into her as I push down on her stomach."
        chizu "Ah, ngh, mm."
        "Chizu's abs twitch. Moaning quietly, she squeezes her arms around me."
        chizu "Mm, aah..."
        "Her body is tense in my arms as she clings desperately to me."
        "I lean in just in time to hear her gasp."
        chizu "Rino! Yes!"
        "Her breath wafts across my ear as her stomach tenses and her hips buck."
        chizu "Aah▼ Nhaah!"
        "Her hips jerk as she squirts, and I see her cloudy juices seeping out of her panties to stain the front of her trousers."
        "She sticks out her tongue, bringing it close to my nipple, but not touching it. Then, with her gaze locked on mine, she points her tongue and flicks it."
        chizu "Ngh, aah..."
        chizu "Nngh, haah."
        "Her tongue runs over my nipple, making a smooching sound; then she presses down on it, and my hips buck in response."
        chizu "Ah▼ Nngh!"
        "Her fingertips slide up my thigh. My gown comes undone, laying me bare to her."
        chizu "Mm, haahm. Does that feel good, Rino?"
        chizu "Aah, ngh, ah▼ I'm—haah. Yes, it feels goo—nhaah, ahngh▼"
        "Heat surges within me and I quiver. But Chizu quickly pins my hips down as an intense climax rips through me."
        chizu "Haah, ah, mmph."
        "Chizu's stomach presses down on me as my hips jerk and my shorts become sodden with my juices."
        chizu "Ah, ah▼"
        "She takes the hardened pebble of my nipple between her lips and flicks her tongue over it."
        "The indulgent motions of her tongue make my stomach tense, and more liquid gushes out of me."
        chizu "Ahn..."
        chizu "Mmph, mm, haah."
        "I can feel the slick liquid sliding down my butt crack, the cold of my sodden shorts stirring a sense of humiliation."
        "Drawn out by her blue eyes, the heat that should have abated surges back, and my heart races."
        "My palm is sweaty against hers, but it feels good."
        chizu "Ah, nhaah. Chizu... Ah!"
        "The look in her eyes and the way she's teasing me like a long, drawn out confession make my insides spasm again."
        "Chizu captures my lips with hers, like she's trying to swallow my moans."
        chizu "Mm, mmph."
        chizu "Ah, nngh!"
        "I climax lightly. My head feels mushy, but Chizu's gaze brings the heat back. My stomach tenses again, and it feels like I'm having one continuous orgasm."
        chizu "Can I give you more?"
        chizu "Haah, mmph, ah... Yes."
        "When her fingers trace the gusset of my panties, I nod then lift my hips so she can slide my underwear down."
        "She briefly moves away to toss them aside, but then her skin is back against mine. I can hear her heartbeat as her fingers brush my clitoris."
        chizu "Ah, ah▼ Nhaah, ahngh!"
        "She licks my lips like she's scooping up my moans as she gently stimulates me."
        "Her tongue probes between my lips while she caresses between my legs."
        "I buck my hips, wanting more than this frustrating teasing, and her eyes crinkle with a smile."
        chizu "You want me to try something else?"
        chizu "Mmph, ah▼ Chizu... Want your fingers... Mm, ah."
        "I squirm desperately, but she keeps her fingers on top, moving them in time with my thrusts."
        chizu "Ah, hyah▼ Ah, aah, mmm▼"
        chizu "You're so cute. Mm. Seeing you like this turns me on."
        chizu "Yes... Ahngh, nngh!"
        "Heat blazes in her eyes as she stares at me, leading me higher with her gaze alone."
        "Then, all at once, her fingers slide inside me."
        chizu "Ah▼ Aah, ngh!"
        "My stomach clenches, and my raised hips slam back to the bed. I shudder beneath the heat of her body."
        chizu "Aah... That's not fair. Ahn!"
        chizu "You're so wet."
        "My inner walls suck desperately at her fingers like I've been starving for them; my entire body is rigid, not given even a moment to relax."
        chizu "Aah, haah, nhaah▼ Yes, ah, ngh. Nhaah, hyaah▼"
        "It's so hot, so good... I feel like I'm gonna lose it. I grip her hand tightly, and she squeezes back in answer."
        "My body shudders, and I realize she's moving her fingers faster, stimulating me harder."
        rino "(Wow... She's actually pretty naughty.)"
        "When she curls her finger inside me, my walls tighten. It's too late for regrets now—my legs instinctively wrap around Chizu's body, trapping her between them."
        chizu "Yes, Chizu, right there! Nhaah! That feels so good▼"
        chizu "Yeah, it's all swollen."
        chizu "Hyah, ah, ah, nngh▼ Ah, aah!"
        chizu "Good girl. Will you tell me how you like it?"
        "Her lips curve upward, and she lets out a little sigh. Then, leaning her weight down on me, she pushes deeper in."
        chizu "Ah, haah, Chizu, yes, so good!"
        chizu "Yeah, I figured."
        chizu "Love what you're, ah, ngh, doing with your fingers. Chizu!"
        "I squeeze the words out, but I feel like my body is doing most of the talking for me as it instinctively does all it can to keep her fingers inside me."
        chizu "Ah, fwah, ahn▼"
        "Her gaze doesn't break from mine the entire time as she touches all my most sensitive spots in just the way I like."
        "My insides spasm at the heat in her eyes."
        "I'm drowning in her heat and her scent, my body shuddering and jerking."
        chizu "Ah, ah▼ Mmph, ah, haah."
        "While my inner squeeze down on her fingers, juices squirt out around them to slide down my ass and thighs."
        "My head buzzes and my vision shimmers, but I keep my eyes open, staring into Chizu's deep blue irises."
        "But then, all of a sudden, she shoves her fingers deep into me again."
        chizu "Ah! Nhaah▼"
        chizu "I wanna hear you moan for me."
        "There's a wet, sticky sound as she pushes down on my clitoris with her palm."
        "The contrast between her sweet tone and violent movements makes me quiver."
        "She's hitting a different angle inside me now."
        "Chizu smiles at this sudden discovery of another weak spot."
        chizu "Aaahn! Ah, I'm coming! Ngh▼"
        chizu "Yeah, that's it. Good girl."
        chizu "Aah, ah, hyah, fwaah..."
        "Hips bucking, I cling to her, pressing myself down onto her fingers and grinding my hips."
        "Heat overtakes my brain, and my consciousness grows hazy. Juices squirt out from between the two fingers buried in my slit."
        chizu "Ah! Hyah! Ah!"
        "My back arches, pushing my clit up into the palm pressing down on it, and shudders wrack my body."

        chizu "...I'm responsible for this."
        "Her voice whispers in my ear and resonates inside me as my boss sliders herself inbetween my parted legs."
        chizu "Wear this."
        "She drapes her blazer over my bare neck."
        "Then she stroker my cheek before reaching down to undo my bra. Her gentle fingers dance over my skin."
        "I fight back the high-pitched moan that tries to escape me."
        chizu "Ah..."
        chizu "Bear with it a little longer."
        "Her fingers slide up my thighs then slowly undo my skirt. Once it's dropped to the floor, she moves on to my underwear."
        chizu "Mm..."
        "I moan, and she looks up at me. When our eyes meet, her deep blue irises shimmer, her painted lips trembling slightly."
        rino "(Here come the butterflies.)"
        "My heartbeat and breathing speed up, and I reach out a hand. When I put it to her neck, her eyes widen and she bites down on her lip."
        rino "(I wish she'd smile at me like she did earlier.)"
        "She turns her gaze away and pulls my panties down before picking up my skirt and carefully placing both articles of clothing on a chair. Then she kneels down before me."
        chizu "Ngh. Boss...?"
        "She wraps her hands around my thighs and presses a kiss to the soft inner flesh."
        rino "(Ah. She's serious about getting me off.)"
        "I meet her gaze again, and the heat in them makes me moan. Her eyes shine like a beast's through the dimness of the room."
        chizu "Mmph."
        chizu "Ah! Ngh, ah... Boss..."
        chizu "Mm, haah."
        "She teasingly traces my lower lips, avoiding my slit, and my hips buck. She pins me in place and kisses beneath my belly button."
        chizu "Mmph, mm. Ngh, yes, right there."
        chizu "Mmph, haah... Maiguma..."
        "I tense my thighs and bury my hands in her long, dark hair. My boss guides one of my legs up to rest on her shoulder, and then she leans in toward my glistening folds."
        chizu "Ah! Ngh, ah, haah... So hot... Ah."
        "She takes my clit between her lips and teases the head with the tip of her tongue. The jolt of pleasure makes my stomach clench."
        "My hips spasm, and there's a wet noise as I press up against her face."
        rino "(Her tongue's so soft and wet. It feels so good!)"
        chizu "Hamph. Stop wriggling."
        chizu "Hngh, ngh. Ah... Yes, there! That's it, ah."
        chizu "Mm... Hah. I know. I won't stop."
        "My mind starts to grow hazy as wet sounds echo around the room. There's a burning heat deep in my stomach, and I cling desperately to my boss as I try to keep still."
        rino "(She's so cute.)"
        "I don't know why that thought comes to me as I trail a finger over the red shell of her ear. She twitches and looks up at me."
        "Her expression is so adorable, I feel my stomach somersault."
        "But the next instant, all thoughts are erased from my mind."
        chizu "Aah! Ngh, mm, yes, nhaah!"
        "She plunges her tongue inside me, and I can't help but push my hips forward, seeking more of the incredible sensation."
        "When I look down, my brain nearly short circuits at the sight of my boss with her face between my legs, tongue buried within me."
        chizu "Aah, ngh... Ah, Boss!"
        "Her tongue hits my sweet spot, and I feel like I'm about to lose it."
        "I move my hips in time with her motions until I feel something hot welling up inside me, then abruptly spill over."
        chizu "Haah, mmph."
        chizu "Ah, haah, aah..."
        "My body goes limp, and I slump forward. As I cling to my boss, I smell the gentle, fresh scent of mint."



        chizu "Mmph... Ngh."
        "The stark white sheets are soft against my skin as I curl into a ball. Tears spill from my eyes, tracking my eyeliner down my face."
        "My hand covers my mouth, the moans escaping from it so wanton I can hardly believe they're coming from me."
        rino "(It's so intense... But is it all because she's my destined mate?)"
        "The warm fuzzy feelings whenever I noticed little things about her, saw the kindness in that pretty face... I'd thought all those feelings were my own."
        "But it was all simply biological instinct determined by my DNA. That truth makes my heart ache, yet I continue to moan desperately."
        chizu "Haah!"
        "I clamp my right hand between my thighs and press down against my stomach. My hips buck up weakly to meet it."
        "There's a wet, slippery sound as my thighs rub together. Biting down on my finger, I screw my eyes shut."
        chizu "Boss... Ngh, haah..."
        "I squeeze my arms against breasts, remembering the tip of her tongue tracing them the day we first met."
        chizu "Ahn..."
        "The thick fabric of my bra pushes back against my nipples. Everything feels so good as I rub myself against the bed."
        "My fingers, supposed to be keeping me quiet, trace my lips then slip into my mouth."
        chizu "Nngh... Ah!"
        "I slide my middle finger further in, pushing down on my tongue, and the pressure makes me moan."
        rino "(No... She wasn't rough like this.)"
        "The images playing behind my eyelids are dim and hazy. I can't recreate her breathy moans or the coolness of her fingertips."
        chizu "Boss..."
        "Though I bury my face in the starchy white hotel pillow, all I can smell is my own shampoo and the scent of my heat."
        "I run a finger over my lips, hoping to find a lingering trace of her scent. My lipstick smears, and I catch the faint, frosty smell of the winter air."
        chizu "Yes, right there..."
        "The words spill from my lips. I screw my eyes shut, trying to follow the scent, acquiescing to my desire and pressing my hand over my shorts."
        chizu "Chizu..."
        "The first time I heard it, I thought it was such a pretty name. I imagined the kind of amazing person it might belong to."
        "My cheeks burn with emotion and desire. I gasp as my stomach clenches deep inside."
        "My womb is crying out for the DNA of an Alpha... of my destined mate. I'm at a loss for what to do as the thought sends more tears coursing down my cheeks."
        chizu "Aah... Chizu!"
        "My hips press up against my hand while I trace my lips with the other."
        chizu "Haah, nhaah! Aah... Chizu! Yes, there!"
        "As I desperately moan her name, the heat building within me spills over."
        chizu "Ngh, ah... Chizu..."
        chizu "Love you..."
        "Abruptly, my hand stills. The words are out there now, echoing in the dim room, and I can't take them back."
        "My inner walls quiver, aching for fingers to fill them, and I let out a long breath as my panties flood with liquid."



        chizu "I don't want you to go! You're MY boss!"
        chizu "Mmph...!"
        chizu "So please... look at me."
        chizu "Just because we're a fated pair, you think my feelings for you aren't real?"
        "Her blue eyes widen and tears well up in them, falling like water droplets. They trail from the corners of her eyes, warming my palms."
        chizu "Even though I care so much for you?"
        chizu "I love you. I want to be with you."
        "I keep her face firmly in place, preventing her from looking away; but then I relax my grip, stroking her cheek."
        chizu "I want to feel your name on my lips. Every little thing I notice about you makes me so happy."
        chizu "...Ms. Maiguma."
        "Her voice is hoarse, her eyes narrowed. Even now, she doesn't try to shake me off as she sits there, tears trailing down her cheeks."
        rino "(She's adorable. I love her so much.)"
        "I push the words back down my throat then bring my lipsticked lips towards her pale pink ones as though I'm being drawn inexorably toward them."
        chizu "You only feel this way because you're in heat."
        chizu "I don't want to hear it."
        chizu "Mm, haah... Wha..."
        chizu "Mm... Haah. So cute."
        "Chizu's lips glitter from the gloss I've transferred to them. I flick the tip of my tongue over them, as though to taste the sparkles."
        chizu "I love you. And I want you to love me back."
        chizu "I want you to tell me I look good when I've done my makeup differently because I knew we'd be working together."
        chizu "Haah, mmph... I understand. Ms. Maiguma, you're..."
        chizu "No, you don't... Chizu."
        "I cut her off. As I stare intently into her eyes, she shuts her mouth, flustered."
        chizu "...Rino?"
        chizu "Yes."
        "My heart swells with joy as her scent strengthens. My pulse races, but it doesn't hurt this time."
        "I put my arms around her, pulling her close and bringing my lips to her neck."
        chizu "Nhaah, mm."
        chizu "Mm, haah."
        "Her hot, damp skin is soft and pliant against my lips. Sucking on it doesn't leave enough of a mark, so I nibble gently instead."
        rino "(Her skin's gone all red.)"
        chizu "Nhaah, mngh."
        chizu "Mmph, ah, haah."
        "I kiss and suck at her neck, trying to leave hickeys, then finish with a gentle bite."
        "Red bruises bloom across her pale skin, dotted with the indentations of my teeth, purplish like the prick of thorns."
        chizu "Since I'm an Omega, I guess biting isn't going to do much."
        "I soothingly kiss the angry welts."
        "Her clavicle stands out prominently above her decolletage, and she trembles slightly as I brush my lips over it."
        chizu "Haah... But this isn't... going to calm your heat."
        "I wrap my arms tightly around her, and she breathes a deep sigh."
        rino "(That's not why I'm doing this.)"
        "Unable to hold back any longer, Chizu moans and leans into me. I capture her lips with mine and feel her hot, wet tongue slide over them."
        chizu "Mm, haha, aah. You're adorable, Chizu."
        chizu "Nhaah, mmph, ah! Nngh."
        "With one hand cupping her cheek, I slide the other around her waist then slip it under her dress to touch her hot, sweaty skin."
        chizu "Mm, aah."
        chizu "You have beautiful breasts."
        "Pushing her dress up, I get a view of her underwear, delicately embroidered with little bluebirds. I stare at the mounds of her breasts then slide a hand under the cup."
        "My fingertips brush a hard nub, and I roll my index finger over it."
        chizu "You're in rut, too."
        "Adorable. Her nipples are smaller than mine, but they're seeking the same stimulation."
        "Heart pounding, I pull the cup aside, and my stomach flips at the sight of her hard, pink nipple peeking out."
        chizu "Haah, mmph, aah."
        "I press down on it, feeling her twitch beneath me, her hands clutching at my back."
        rino "(She likes that.)"
        chizu "Mm, ah... Don't do that."
        chizu "What? You don't like having your nipples teased?"
        "I whisper into her ear, enjoying the way she gasps, her lashes trembling over her downturned eyes."
        "I push down on her nipple again, wanting to see more of her rapturous expressions."
        chizu "I'm gonna—ahn! Ah! Nnngh!"
        chizu "Don't hold back."
        "I run my tongue along her earlobe, avoiding the single gold stud."
        chizu "Haah!"
        "She moans deeply and her scent strengthens. Liquid gushes out of her, staining her white panties."
        "My hips move reflexively, grinding against her."
        rino "(No, I don't wanna be the only one getting off!)"
        chizu "Rino...?"
        "I press my lips to hers as though to capture the heat in her voice."
        chizu "Aah, haah, mm."
        "We moan between kisses. When I push my tongue between her lips, she eagerly accepts it. Our saliva mingles, and her moans send tingles to my tummy."
        "Chizu's eyes shimmer, and a tear trails down her cheek. Then she pulls me closer and twines her tongue around mine."
        chizu "Ngh, mmph ▼ Chizu, ah... You're so cute."
        chizu "Mm, haah, mmph."
        "When I pull away for a moment, Chizu immediately draws me back toward her."
        "A sweet smell surrounds us, her scent mingling with mine. Fire blazes in my belly."
        rino "(I'm sure she's feeling the same way.)"
        "I press my hand to her warm stomach and feel the muscles twitch beneath my palm."
        chizu "Haah, mmph."
        "I trail my finger around her bellybutton then slide it down."
        chizu "Nngh!"
        rino "(Not there. A little lower.)"
        chizu "Aah, nhaah!"
        chizu "That's the spot▼"
        "I push my fingers inward, and her hips buck like she's trying to get away. Holding her  still with one hand, I use my left to dig into the same spot."
        chizu "Nhaah, ah... What are you... Ngh, ahn, ah! I'm—!"
        chizu "Feels good right here, doesn't it?"
        "Just beneath the cervix... When I push on her abdomen, I can tell her inner walls are twitching, desperate for my fingers."
        chizu "What are you... Ah! Nngaah!"
        chizu "I learned to do this to get off when I'm in heat but not in a situation where I can touch myself down there."
        "Her moans are breathy and sensuous. Filled with affection for her, I press a kiss to her cheek."
        chizu "I want more. Don't hold back. Come for me."
        "I rock my hips, leaning my weight into her as I push down on her stomach."
        chizu "Ah, ngh, mm."
        "Chizu's abs twitch. Moaning quietly, she squeezes her arms around me."
        chizu "Mm, aah..."
        "Her body is tense in my arms as she clings desperately to me."
        "I lean in just in time to hear her gasp."
        chizu "Rino! Yes!"
        "Her breath wafts across my ear as her stomach tenses and her hips buck."
        chizu "Aah▼ Nhaah!"
        "Her hips jerk as she squirts, and I see her cloudy juices seeping out of her panties to stain the front of her trousers."


        chizu "Haah... Chizu."
        "Her eyes shimmer with suppressed heat. Her hand tightens on mine, and I feel her hot breath on my face as her scent overwhelms me."
        chizu "I won't leave you."
        "The light catches her collarbone peeking out over black lace. Just imagining the feel of her skin makes heat pool in my stomach."
        "Chizu's fingertips dance around my chest, and out of the corner of my eye, I can see my nipples hardening."
        chizu "Ngh, ah."
        chizu "I've wanted to do this for so long."
        "She squeezes my hand, using her other to tentatively caress my breast."
        "Her perfectly manicured brows knit together in concentration. Her pale pink lipgloss absorbs the light and shimmers captivatingly."
        chizu "Nngh, haah, mm."
        chizu "Mm, haah."
        "She captures my lower lip between hers. Keeping my eyes locked on hers, I hungrily slide my tongue into her mouth."
        chizu "Ngh, haah. Chizu!"
        chizu "Haah, mmph."
        "Her hot tongue feels incredible. We kiss until my lungs feel like they're about to burst."
        "Pleasure shudders down my spine as I point my tongue and lap at the underside of hers, trying to find out what makes her tick."
        chizu "Mm, haah. I love you."
        chizu "Ngh..."
        chizu "How do you feel?"
        chizu "I don't have the same way with words as you do."
        "My heart pounds at the sight of her, so uncertain, and so unlike her calm and collected work demeanor."
        rino "(She's not gonna let go of my hand.)"
        "In place of words, I feel the heat coming from our entwined fingers, and I smile happily."
        chizu "Then I want you to show me with your body."
        chizu "Nhaah. Until I forget all about fate and destiny and all that crap."
        chizu "You really want me to let loose on you?"
        "As though in response, I feel liquid gushing from between my legs."
        chizu "Mm, ahm. Yes."
        chizu "Tell me if it gets too much."
        "I smile to allay her concern."
        chizu "I'm not the weak little Omega you seem to think I am."
        chizu "Then I suppose I'm not the big strong Alpha you think I am, either."
        "Her eyes narrow with relief, and then she lowers her face to my chest."
        "She sticks out her tongue, bringing it close to my nipple, but not touching it. Then, with her gaze locked on mine, she points her tongue and flicks it."
        chizu "Ngh, aah..."
        chizu "Nngh, haah."
        "Her tongue runs over my nipple, making a smooching sound; then she presses down on it, and my hips buck in response."
        chizu "Ah▼ Nngh!"
        "Her fingertips slide up my thigh. My gown comes undone, laying me bare to her."
        chizu "Mm, haahm. Does that feel good, Rino?"
        chizu "Aah, ngh, ah▼ I'm—haah. Yes, it feels goo—nhaah, ahngh▼"
        "Heat surges within me and I quiver. But Chizu quickly pins my hips down as an intense climax rips through me."
        chizu "Haah, ah, mmph."
        "Chizu's stomach presses down on me as my hips jerk and my shorts become sodden with my juices."
        chizu "Ah, ah▼"
        "She takes the hardened pebble of my nipple between her lips and flicks her tongue over it."
        "The indulgent motions of her tongue make my stomach tense, and more liquid gushes out of me."
        chizu "Ahn..."
        chizu "Mmph, mm, haah."
        "I can feel the slick liquid sliding down my butt crack, the cold of my sodden shorts stirring a sense of humiliation."
        "Drawn out by her blue eyes, the heat that should have abated surges back, and my heart races."
        "My palm is sweaty against hers, but it feels good."
        chizu "Ah, nhaah. Chizu... Ah!"
        "The look in her eyes and the way she's teasing me like a long, drawn out confession make my insides spasm again."
        "Chizu captures my lips with hers, like she's trying to swallow my moans."
        chizu "Mm, mmph."
        chizu "Ah, nngh!"
        "I climax lightly. My head feels mushy, but Chizu's gaze brings the heat back. My stomach tenses again, and it feels like I'm having one continuous orgasm."
        chizu "Can I give you more?"
        chizu "Haah, mmph, ah... Yes."
        "When her fingers trace the gusset of my panties, I nod then lift my hips so she can slide my underwear down."
        "She briefly moves away to toss them aside, but then her skin is back against mine. I can hear her heartbeat as her fingers brush my clitoris."
        chizu "Ah, ah▼ Nhaah, ahngh!"
        "She licks my lips like she's scooping up my moans as she gently stimulates me."
        "Her tongue probes between my lips while she caresses between my legs."
        "I buck my hips, wanting more than this frustrating teasing, and her eyes crinkle with a smile."
        chizu "You want me to try something else?"
        chizu "Mmph, ah▼ Chizu... Want your fingers... Mm, ah."
        "I squirm desperately, but she keeps her fingers on top, moving them in time with my thrusts."
        chizu "Ah, hyah▼ Ah, aah, mmm▼"
        chizu "You're so cute. Mm. Seeing you like this turns me on."
        chizu "Yes... Ahngh, nngh!"
        "Heat blazes in her eyes as she stares at me, leading me higher with her gaze alone."
        "Then, all at once, her fingers slide inside me."
        chizu "Ah▼ Aah, ngh!"
        "My stomach clenches, and my raised hips slam back to the bed. I shudder beneath the heat of her body."
        chizu "Aah... That's not fair. Ahn!"
        chizu "You're so wet."
        "My inner walls suck desperately at her fingers like I've been starving for them; my entire body is rigid, not given even a moment to relax."
        chizu "Aah, haah, nhaah▼ Yes, ah, ngh. Nhaah, hyaah▼"
        "It's so hot, so good... I feel like I'm gonna lose it. I grip her hand tightly, and she squeezes back in answer."
        "My body shudders, and I realize she's moving her fingers faster, stimulating me harder."
        rino "(Wow... She's actually pretty naughty.)"
        "When she curls her finger inside me, my walls tighten. It's too late for regrets now—my legs instinctively wrap around Chizu's body, trapping her between them."
        chizu "Yes, Chizu, right there! Nhaah! That feels so good▼"
        chizu "Yeah, it's all swollen."
        chizu "Hyah, ah, ah, nngh▼ Ah, aah!"
        chizu "Good girl. Will you tell me how you like it?"
        "Her lips curve upward, and she lets out a little sigh. Then, leaning her weight down on me, she pushes deeper in."
        chizu "Ah, haah, Chizu, yes, so good!"
        chizu "Yeah, I figured."
        chizu "Love what you're, ah, ngh, doing with your fingers. Chizu!"
        "I squeeze the words out, but I feel like my body is doing most of the talking for me as it instinctively does all it can to keep her fingers inside me."
        chizu "Ah, fwah, ahn▼"
        "Her gaze doesn't break from mine the entire time as she touches all my most sensitive spots in just the way I like."
        "My insides spasm at the heat in her eyes."
        "I'm drowning in her heat and her scent, my body shuddering and jerking."
        chizu "Ah, ah▼ Mmph, ah, haah."
        "While my inner squeeze down on her fingers, juices squirt out around them to slide down my ass and thighs."
        "My head buzzes and my vision shimmers, but I keep my eyes open, staring into Chizu's deep blue irises."
        "But then, all of a sudden, she shoves her fingers deep into me again."
        chizu "Ah! Nhaah▼"
        chizu "I wanna hear you moan for me."
        "There's a wet, sticky sound as she pushes down on my clitoris with her palm."
        "The contrast between her sweet tone and violent movements makes me quiver."
        "She's hitting a different angle inside me now."
        "Chizu smiles at this sudden discovery of another weak spot."
        chizu "Aaahn! Ah, I'm coming! Ngh▼"
        chizu "Yeah, that's it. Good girl."
        chizu "Aah, ah, hyah, fwaah..."
        "Hips bucking, I cling to her, pressing myself down onto her fingers and grinding my hips."
        "Heat overtakes my brain, and my consciousness grows hazy. Juices squirt out from between the two fingers buried in my slit."
        chizu "Ah! Hyah! Ah!"
        "My back arches, pushing my clit up into the palm pressing down on it, and shudders wrack my body."



        chizu "Honestly, Boss, you're not very Alpha-like."
        chizu "Really? Mm, I suppose I'm not really a natural-born leader."
        chizu "...Although you go super Alpha mode during sexy times."
        chizu "Huh? I do?"



        chizu "How many Alphas are there in our company anyway?"
        chizu "I don't know the exact number, but I think there's a lot at the managerial level, and then everyone else is mostly Betas."
        chizu "Hmm, I suppose it makes sense that there'd be a lot of Betas. I guess most of my friends are Betas, too."



        chizu "Seriously, there's nothing good about being born an Omega. I get stared at on the street, and when I go into heat I've gotta hide myself away from everyone."
        chizu "Your mom is an Omega, too, right?"
        chizu "Yeah, so I guess I got a lot of my tricks and evasive maneuvers from her. I've made it this far, at least!"
        chizu "...She sounds like a good mom."
        rino "(Uh-oh, she looks concerned. Maybe she's even more of a worrier than my own mother!)"



        chizu "I know you don't like to miss work, but it must be difficult to concentrate during your heat, and you have dedicated leave for it..."
        chizu "Hmm, I feel like people would say it's not fair for me to get time off just for being an Omega."
        chizu "Don't worry about that. I take time off for migraines or when I'm having a bad period."
        chizu "Also, if I'm in heat, even just calling to say I'm taking the day off and hearing your voice down the phone would, uh..."
        chizu "Oh, r-right. Well, you can call someone else instead."
        chizu "Okaaay."


        chizu "I keep mine hidden behind my employee ID in my pass holder!"


        chizu "A lot of Omegas wear clothing that covers up their neck since they're scared of being bitten."
        chizu "But your shoulders are bare?"
        chizu "Yeah, because I think I have really nice shoulders! Wouldn't it be a shame to keep them covered up?"
        chizu "I mean, yeah, they're nice, but they do have an effect..."
        chizu "Boss?"
        chizu "Uh, but you're free to do whatever you like."


        chizu "The theme of Destined Mates is super popular. There was that recent TV show about infidelity, wasn't there?"
        chizu "And it's even been used in makeup marketing campaigns..."
        chizu "Oh! I saw that! The powder with the slogan, 'Dust On Your Destiny'?"
        chizu "Hehe. What did you think of it?"
        chizu "Love it! It makes my complexion look great and sets my foundation in place... Wait, is finding your makeup holy grain basically like finding your Destined Mate...?"
        chizu "Mm, I wouldn't say they're the same..."

    rino "Okay, I have my heat suppressant, and the draft is good to go!"
    "I check that my pill case is in my bag, check my laptop screen one last time, then nod to motivate myself."
    "I've already given my statement to the police, so now it's time to get back to the office and carry on with my work."
    "But in the mirror, Chizu's expression is concerned. She looks younger than usual, maybe because she hasn't done her makeup yet."
    chizu "There's no point in going all the way back to the office. Why don't you head straight home? You must be exhausted."
    rino "You worry too much, Chizu."
    chizu "That's... probably true."
    "Chizu trails off. I giggle then clasp my hands together and speak cheerily."
    rino "Besides, I wanna get this article finished ASAP."
    "Chizu's expressions softens and she looks down, pressing her fingers to her lips."
    chizu "Oh."
    rino "(Hehe, she's so cute.)"
    "It's a gesture at odds with the competent editor-in-chief I see at work, and my heart skips a beat."
    "I murmur quietly to myself."
    rino "If you're that worried, you should've gone ahead and claimed me."
    chizu "Rino."
    rino "Oh, you heard that?"
    "Her tone is sharper than usual."
    "Chizu isn't the type of woman to claim someone just because they're her lover."
    "That's clearly not who she is."
    chizu "Don't say things like that, even as a joke."
    "For a moment I think she's angry, but then the scent of mint wafts over me."
    "From behind me, Chizu pulls me closer to her and runs her fingers through my hair before bringing her lips to my nape."
    rino "(Her face is so hot.)"
    "She brushes her lips over the skin there, not leaving a mark; but the expression I can see on her face through the mirror makes my pulse race."
    chizu "There's something more important to me than mating right now, so let me have that, okay?"
    "Her voice is gentle. Smiling, I press my hand to my chest; it aches, but somehow it's not painful."
    "When I nod, Chizu closes her eyes and nuzzles against my cheek. Her heartbeat reverberates through the still morning air, and I lightly bite down on my lip."
    rino "...Okay."
    "Chizu pulls me against her, and the motion causes her jacket to slide down her shoulder. I gulp at the sight of her bare throat in the mirror."
    "My eyes are drawn to the gold chain resting against her decolletage, and then my glossy lips curl into a smile."
    "There's a mark on Chizu's throat."
    "It's a lustrous pink, standing out vividly against her pale skin like a lipstick stain."

    $ renpy.movie_cutscene("videos/liptrip_ed_en.mpgv")

    return
