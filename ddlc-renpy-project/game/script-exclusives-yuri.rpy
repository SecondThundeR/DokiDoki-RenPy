label yuri_exclusive_1:

    scene bg club_day
    with wipeleft_scene

    "I'm really curious to talk to Yuri a little bit more..."

    "But at the same time, I would feel bad for distracting her from reading."

    "I catch a glimpse of the cover of her book."

    "It looks like the same book that she lent to me..."

    "More than that, she seems to be on the first few pages."

    play music t6 fadeout 1.0

    show yuri 4a zorder 2 at t11

    y "Ah..."

    "Crap--"

    "I think she noticed me looking at her..."

    "She sneaks another glance at me, and our eyes meet for a split second."

    y 4b "..."

    "But that only makes her hide her face deeper in her book."

    mc "Sorry..."

    mc "I was just spacing out..."

    "I mutter this, sensing I made her uncomfortable."

    y 1i "Oh..."

    y "It's fine..."

    y 1a "If I was focused, then I probably wouldn't have noticed in the first place."

    y "But I'm just re-reading a bit of this, so..."

    mc "That's the book that you gave me, right?"

    y "Mhm."

    y "I wanted to re-read some of it."

    y 2q "Not for any particular reason...!"

    mc "Just curious, how come you have two copies of the same book?"

    y "Ah..."

    y "Well, when I stopped at the bookstore yesterday--"

    y 3o "Ah, that's not what I meant..."

    y "I mean--"

    y 1w "I...just happened to buy two of them."

    mc "Ah, I see."

    "There's something fairly obvious here that Yuri isn't telling me, but I decide to let it go."

    mc "I'll definitely start reading it soon!"

    y 2u "I'm glad to hear..."

    y "Once it starts to pick up, you might have a hard time putting it down."

    y 2c "It's a very engaging and relatable story."

    mc "Is that so...?"

    mc "What's it about, anyway?"

    y 1f "Well..."

    y "Mmm..."

    "Yuri closes the book and scans her eyes over the back."

    "The book is titled \"Portrait of Markov\"."

    "There's an ominous-looking eye symbol on the front cover."

    y 1a "Alright..."

    y "I just wanted to make sure I don't accidentally give anything away."

    y "Basically, it's about this girl in high school who moves in with her long-lost younger sister..."

    y "But as soon as she does so, her life gets really strange."

    y 1m "She gets targeted by these people who escaped from a human experiment prison..."

    y "And while her life is in danger, she needs to desperately choose who to trust."

    y 1i "No matter what she does, she ends up destroying most of her relationships and her life starts to fall apart..."

    mc "That's kind of--!"

    "That's kind of dark, isn't it?"

    "Yuri made it sound like it was going to be a nice story, so that dark turn came from nowhere."

    y 1c "Ahaha."

    "Yuri gently giggles, all of a sudden."

    y "Are you not a fan of that sort of thing, [player]?"

    mc "No, it's not that..."

    mc "I mean, I can definitely enjoy those kinds of stories, so don't worry."

    y 2u "I hope so..."

    "Yeah... I totally forgot that Yuri is into those things."

    "She's so shy and reclusive on the outside, but her mind seems to be completely different."

    y "It's just that those kinds of stories..."

    y 1a "They challenge you to look at life from a strange new perspective."

    y "When horrible things happen not just because someone wants to be evil..."

    y 1m "But because they have their own goals, or their own philosophy that they believe in."

    y "Then suddenly, when you thought you related to the protagonist..."

    y "They're made out to be the naive one for letting their one-sided morals interfere with the villain's plans."

    y 3v "I'm...I'm rambling, aren't I...?"

    y "Not again..."

    y 4b "I'm sorry..."

    mc "Hey, don't apologize...!"

    mc "I haven't lost interest or anything."

    y "Well..."

    y "I guess it's alright, then..."

    y 4a "But I feel like I should let you know that I have this problem..."

    y "When I let things like books and writing fill my thoughts..."

    y "I kind of forget to pay attention to other people..."

    y 3t "So I'm sorry if I end up saying something strange!"

    y "And please stop me if I start talking too much!"

    mc "That's--"

    mc "I really don't think you need to worry..."

    mc "That just means you're passionate about reading."

    mc "The least I can do is listen."

    mc "It's a literature club, after all..."

    y 4a "Ah--"

    y "That's..."

    y "Well, that's true..."

    mc "In fact..."

    mc "I might as well get started reading it, right?"

    y 3n "Y-You don't have to!"

    mc "Ahaha, what are you saying?"

    mc "Just a moment ago, you said you were looking forward to it."

    y 3o "..."

    mc "Let me just get the book..."

    "I quickly retrieve the book that I had put into my bag."

    mc "Alright...it's fine if I sit here, right?"

    "I slip into the seat next to Yuri's."

    y 3n "Ah...!"

    y "Yeah..."

    mc "Are you sure?"

    mc "You seem a little apprehensive..."

    y "That's..."

    y 4b "I'm sorry..."

    y "It's not that I don't want you to!"

    y "It's just something I'm not very used to..."

    y "That is, reading in company with someone."

    mc "I see..."

    mc "Well, just tell me if I end up distracting you or anything."

    y "A-Alright..."

    show yuri zorder 1 at thide
    hide yuri

    "I open the book and start the prologue."

    "I soon understand what Yuri means about reading in company."

    "It's as if I can feel her presence over my shoulder as I read."

    "It's not a particularly bad thing."

    "Maybe a little distracting, but the feeling is somewhat comforting."

    "Yuri is in the corner of my eye."

    "I realize that she's not actually looking at her own book."

    "I glance over."

    "It looks like she's reading from my book instead--"

    show yuri 3n zorder 2 at t11

    y "S-Sorry!"

    y "I was just--!"

    mc "Yuri, you really apologize a lot, don't you?"

    y "I...I do?"

    y 4a "I don't really mean to..."

    y "Sorry..."

    y 4c "I mean--!"

    mc "Ahaha."

    mc "Here, this should work, right?"

    "I slide my desk until it's up against Yuri's, then hold my book more between the two of them."

    y 2v "Ah..."

    y "I suppose so..."

    "Yuri timidly closes her own copy."

    "Once we each lean in a little bit, our shoulders are almost touching."

    "It feels like my left arm is in the way, so instead I use my right hand to hold the book open."

    mc "Ah, I guess that makes it kind of difficult to turn the page..."

    y "Here..."

    $ persistent.clear[2] = True

    $ renpy.save_persistent()

    scene y_cg1_base with dissolve_cg

    "Yuri takes her left arm and holds the left side of the book between her thumb and forefinger."

    mc "Ah..."

    "I do the same with my right arm, on the right side of the book."

    "That way, I turn a page, and Yuri slides it under her thumb after it flips to her side."

    "But in holding it like this..."

    "We're huddled even closer together than before."

    "It's actually kind of distracting me...!"

    "It's as if I can feel the warmth of Yuri's face, and she's in the corner of my vision..."

    show y_cg1_exp1 at cgfade

    y "...Are you ready?"

    mc "Eh?"

    y "To turn the page..."

    mc "Ah...sorry!"

    mc "I think I got a bit distracted for a second..."

    "I glance over at Yuri's face again, and our eyes meet."

    "I don't know how I'll be able to keep up with her..."

    y "Ah..."

    show y_cg1_exp2 at cgfade

    y "That's okay."

    y "You're not as used to reading, right?"

    y "I don't mind being patient if it takes you a bit longer..."

    y "It's probably the least I can do..."

    y "Since you've been so patient with me..."

    mc "Y-Yeah..."

    mc "Thanks."

    hide y_cg1_exp1
    hide y_cg1_exp2

    "We continue reading."

    "Yuri no longer asks me if I'm ready to turn the page."

    "Instead, I just assume that she finishes the page before me, so I turn it by my own volition."

    "We continue the first chapter in silence."

    "Even so, turning each page almost feels like an intimate exchange..."

    "My thumb gently letting go of the page, letting it flutter over to her side as she catches it under her own thumb."

    mc "Hey, Yuri..."

    mc "This might be a silly thought, but..."

    mc "The main character kind of reminds me of you a little bit."

    show y_cg1_exp1 at cgfade

    y "You...think so?"

    y "How does she?"

    mc "Well, I guess she's more blunt in a lot of ways..."

    mc "But she also second-guesses all of the things that she says and does."

    mc "Like she's afraid she'll do something wrong."

    mc "It's not like I can see into your head or anything..."

    mc "But they're kind of reminiscent of some of your mannerisms."

    y "I-I see..."

    scene bg club_day
    show yuri 2t zorder 2 at i11
    with dissolve_cg

    "Yuri remains silent for a moment."

    y "But [player]..."

    y "That's probably..."

    y "...a terrible thing to have in common with her!"

    y 4b "Uuuh, that's so embarrassing that you think that..."

    mc "W-Wait!"

    mc "I didn't mean it in a bad way or anything!"

    mc "Sorry, I really didn't know you were self-conscious about that sort of thing..."

    y "..."

    mc "I guess I more meant that it's kind of cute..."

    y 3q "A-Ah--"

    y "What are you saying all of a sudden...?"

    y "I...!"

    show monika 4 at l31

    m "Okay, everyone!"

    show yuri 3n at h11

    y "...!"

    show monika zorder 3 at f31

    m "I think it's about time we share today's poems with each other."

    m "We might not have enough time if we wait too long."

    show monika zorder 2 at t31
    show yuri zorder 3 at f11

    y 3w "Ah..."

    "Yuri exhales, spared from finishing her thought."

    show yuri zorder 2 at t11
    show monika zorder 3 at f31

    m 1 "Is that alright, Yuri?"

    m "You look kind of down..."

    m "I'm sorry if you haven't been looking forward to this..."

    show monika zorder 2 at t31
    show yuri zorder 3 at f11

    y 3v "Ah, it's not..."

    y "...It's fine."

    show yuri zorder 2 at t11
    show monika zorder 1 at thide
    hide monika

    "Yuri releases her hand from the book, causing it to close on top of my thumb."

    mc "Alright..."

    mc "I guess I'll do some more reading tonight."

    mc "Or would you prefer I only read it with you?"

    y 2f "Um...!"

    y "I...guess I don't have too much of a preference either way..."

    mc "Hmm..."

    mc "In that case, I'll read a little more tonight."

    mc "It'll be more fun to read with you after it picks up a bit, you know?"

    y 2a "That's good reasoning."

    y "In that case, feel free to finish the first two chapters in your own time."

    mc "Alright!"

    show yuri zorder 1 at thide
    hide yuri

    "I stand up."

    "I make a mental note of where I left off in the book, then slip it back into my bag."

    return

label yuri_exclusive_2:

    $ y_exclusivewatched = True

    play music t6 fadeout 1.0

    scene bg club_day
    with wipeleft_scene

    mc "Hey, Yuri."

    show yuri 2f zorder 2 at t11

    y "Eh?"

    mc "Ah..."

    "I suddenly notice that Yuri is reading a different book from the one we've been reading together."

    mc "Sorry! I didn't mean to interrupt..."

    y 2m "Ah, no..."

    y "I was kind of just waiting for you..."

    show yuri 2a

    mc "Ah, if that's the case..."

label yuri_exclusive_2_ch3:

    mc "Why don't we go ahead and get started?"

    y 2c "Yes, let's!"

    y 3a "Actually, I have a request..."

    y "...Do you mind if I make some tea first?"

    mc "Not at all."

    y 1c "Thanks very much."

    y 1a "If there's one thing that can make my reading time here any better, it's a nice cup of tea."

    y "Not to mention for yourself, as well."

    show yuri zorder 1 at thide

    hide yuri

    "Yuri stands up and makes her way to the closet."

    "I follow and watch as she retrieves a small water pitcher from the shelf - the kind with a filter inside."

    show yuri 1f zorder 2 at t11

    y "Can you hold this for a second?"

    mc "Sure..."

    "Yuri hands me the water pitcher and also fetches an electric kettle."

    y "I'm going to plug this in at the teacher's desk, and then we'll go get some water."

    show yuri zorder 1 at thide
    hide yuri

    "She walks past me and sets the kettle down on the teacher's desk."

    "I simply watch her movements."

    "To my surprise, the way she moves really contrasts her speaking mannerisms."

    "Especially because of her long legs, Yuri appears elegant and methodical."

    show yuri 1f zorder 2 at t11

    y "Okay, may I have the water pitcher?"

    y 1a "Thanks. I'll be right back."

    mc "Ah, I might as well walk with you..."

    y 1s "Yeah...why not?"

    y "Shall we go, then?"

    mc "Yeah..."

    show monika 2a at l31

    m "Hm? Where are you two off to?"

    show yuri 2e

    mc "Eh?"

    mc "We're just...Yuri was going to make some tea, so..."

    "I suddenly realize how weird it sounds to explain this to Monika."

    mc "We're just filling the water pitcher..."

    show monika zorder 3 at f31

    m "Ah, okay!"

    m 4j "Sorry, I was just a bit curious..."

    m "That's kind of a one-person job, isn't it?"

    show monika 4a zorder 2 at t31

    mc "That's--"

    show yuri zorder 3 at f11

    y 1k "Monika, please mind your own business for once."

    y "Or do you want to tell me there's something wrong with helping involve [player] in club activities?"

    show yuri zorder 2 at t11
    show monika zorder 3 at f31

    m 1g "E-Eh...?"

    show monika zorder 2 at t31

    mc "--!"

    "My mouth gapes."

    show monika zorder 3 at f31

    m 5a "I..."

    m "I suppose there's nothing wrong with that..."

    show monika zorder 2 at t31
    show yuri zorder 3 at f11

    y 2l "Hmph..."

    y "Then let's go, [player]."

    show yuri zorder 2 at t11

    mc "Ah..."

    "Yuri quickly exits the room, and I follow."

    stop music fadeout 1.0

    scene bg corridor
    show yuri 4c zorder 2 at t11
    with wipeleft_scene

    "Once in the hallway, she suddenly puts her forehead against the wall."

    y "I spoke without thinking..."

    y "How could I say something like that...?"

    mc "Yuri..."

    y 4b "I just..."

    y "Something about the way she said that..."

    y "It made me feel so...irritated."

    y "What's wrong with me...?"

    mc "No, Yuri."

    mc "I think...you did the right thing!"

    mc "I wasn't expecting it, but..."

    mc "It's also not right for Monika to judge people like that."

    play music t9

    y 4a "[player]..."

    y "How come even when I do something bad..."

    y "You're being nice to me?"

    mc "Because."

    mc "Nothing that you do is as bad as you make it seem in your head."

    mc "Nobody's perfect."

    mc "We have emotions, and we can't always hide them away."

    mc "But you always amplify things in your head..."

    mc "Your mind turns a light rain shower into a hurricane."

    y 3q "Ah..."

    y "N-No..."

    y "Wouldn't you hate me for something as terrible as that...?"

    mc "Why would I hate you?"

    mc "I can't hate someone for having emotions..."

    mc "What kind of friend would do that?"

    y 4c "Friend...you say?"

    y "Ah...um..."

    "Yuri lifts her head."

    y 3w "[player]..."

    y 3t "I really like...being friends with you!"

    mc "Ahaha..."

    mc "Thanks, Yuri."

    mc "I like being friends with you too..."

    "I feel kind of awkward saying something like that..."

    "But I'm doing my best to help Yuri feel better."

    mc "Anyway...!"

    y 3u "Ah-- Yeah..."

    y "Shall we go?"

    mc "Yeah."

    show yuri zorder 1 at thide
    hide yuri

    "Yuri and I walk to the nearest water fountain."

    "Once we fill up the water pitcher, we return to the classroom."

    play music t6 fadeout 1.0

    scene bg club_day
    show yuri 1a zorder 2 at t11
    with wipeleft_scene

    y "[player], do you like oolong tea?"

    mc "Ah, yeah."

    mc "Anything is fine."

    y "Very well."

    "Yuri sets the temperature on the kettle to 200 degrees."

    y 1f "Now it's time to get the teapot."

    mc "You really do this properly, don't you?"

    y 1u "Of course..."

    y "I shouldn't do any less when I'm making tea for others."

    mc "Even if I'm not an expert on tea or anything...?"

    y 2m "Huhu."

    y 2a "In that case, you'll only be even more impressed."

    mc "Ah...perhaps I will!"

    show yuri zorder 1 at thide
    hide yuri

    "Yuri fetches the teapot and begins measuring the tea leaves."

    "To my surprise, she even starts humming a little to herself."

    show yuri 1c zorder 2 at t11

    mc "You must be in a good mood now..."

    y 1a "Is that so?"

    y "I was letting it show..."

    y "And you noticed."

    y 2u "I was doing a bit of thinking..."

    y "And I decided that I would try expressing myself a little bit more."

    y "It turns out it's not very hard for me to do..."

    y 1c "When it's you who's around, anyway."

    mc "Ah..."

    mc "That's great, Yuri!"

    mc "Just don't push yourself too much."

    y 3u "You're always worrying about me, [player]..."

    y "It's very endearing."

    mc "That's..."

    "Yuri wasn't kidding..."

    "I don't even know if I can keep up with this...!"

    "I watch Yuri pour a cup of tea for each of us."

    y 1a "[player], I have another request."

    y "Do you mind if we sit on the floor today?"

    mc "Eh? Why's that?"

    y 1h "It's a little bit easier on my back..."

    y "I can read with my back against the wall rather than bending over at my desk."

    mc "Ah, sorry, I didn't realize."

    y 1a "No worries."

    y "I just have back pain fairly regularly, so I do my best to manage it."

    mc "Is that so?"

    mc "I wonder why that is..."

    y 1f "It's most likely because my--"

    y 1n "Ah--"

    y 1o "M-My..."

    mc "Your posture, right?"

    mc "Always hunched over like that while reading..."

    y 2p "Yes!"

    y 2q "I have terrible reading posture!"

    y "So that's why we should sit on the floor."

    mc "Fair enough."

    mc "I'll go ahead and get the book."

    show yuri zorder 1 at thide
    hide yuri

    "I retrieve the book from my bag."

    mc "Ah, I have some chocolate as well..."

    "It's a bag of small chocolate candies that I kept hidden from Sayori's candy radar."

    "I take it, since it'll go well with the tea."

    "Yuri and I then sit against the wall, teacups at our sides."

    "As if in sync, we assume the same reading position as last time, each holding one half of the book."

    "Except this time..."

    "Our bodies are even closer to each other."

    show yuri 2h zorder 2 at t11

    y "I can't see too well..."

    mc "--!"

    show yuri 2e at d11

    "Yuri slides closer until our shoulders are touching."

    "How am I supposed to focus on reading like this...?!"

    "Yuri was always kind of cute, but..."

    "When she's being less apprehensive, it's almost more than I can handle!"

    y 2f "Your teacup..."

    "Yuri hands me my teacup."

    "Holding it with my hand that's not holding the book, I end up in a position that makes it even harder to focus."

    "Because now I need to worry about making sure I don't accidentally touch her chest...!"

    "Meanwhile, Yuri hasn't noticed a single thing."

    "She wears her intense reading expression, and I can only presume the world around her has faded away."

    "I use all of my willpower to focus on reading."

    "..."

    "After a few minutes, I finally manage to relax a little."

    "I put the teacup between my legs and fumble with the chocolate wrapper."

    mc "Ah, sorry..."

    "I briefly let go of the book to finish opening the wrapper."

    mc "You can have as much as you want."

    y 2s "Ah, that's..."

    y "That's okay, I won't take any..."

    mc "Eh? Are you sure?"

    y 2v "Well..."

    y "If I touch it, then it might get smudges on the pages..."

    mc "Ah, you're right..."

    mc "I didn't even think about that."

    mc "My bad..."

    y 2a "No need to apologize."

    y "I'll hold the book, okay?"

    mc "Are you sure...?"

    y "Of course."

    $ persistent.clear[3] = True

    $ renpy.save_persistent()

    scene y_cg2_bg
    show y_cg2_base
    show y_cg2_details
    show y_cg2_nochoc
    show y_cg2_dust1
    show y_cg2_dust2
    show y_cg2_dust3
    show y_cg2_dust4
    with dissolve_cg

    "Yuri opens the book with both hands."

    "She holds it so that I don't have any harder of a time reading from it."

    "But as a result, her left arm is practically resting on top of my leg."

    mc "Well, in that case..."

    "Yuri is already totally focused on reading again."

    "I take a chocolate candy and pop it into my mouth."

    "Then, I take another chocolate..."

    "And I hold it up to Yuri."

    "She doesn't even look away from the book."

    "She simply parts her lips, as if this situation was completely natural."

    "But that means I can't stop here!"

    hide y_cg2_nochoc

    "I apprehensively place the chocolate in her mouth."

    "Just like that, Yuri closes her lips over it."

    y "Eh...?"

    show y_cg2_exp2

    "Yuri's expression suddenly breaks."

    y "Did..."

    y "Did I just..."

    "Yuri looks at me like she needs to confirm what just happened."

    show y_cg2_exp3
    show y_cg2_nochoc:
        alpha 0
        linear 0.5 alpha 1
    hide y_cg2_exp2

    y "U-Um..."

    y "[player]..."

    mc "S-Sorry!"

    mc "I guess I shouldn't have done that..."

    y "Ah, that's..."

    y "Well..."

    y "Y-You were just helping..."

    y "That's something that...friends do..."

    y "...Right?"

    mc "I mean..."

    "Not really in this kind of context, but..."

    mc "Yeah..."

    mc "...That's all it was."

    y "Yeah..."

    y "Then..."

    y "You don't need to stop or anything..."

    mc "I-I see..."

    hide y_cg2_exp3

    "The situation has gotten really tense..."

    "Yuri tries to return to the book."

    "But I can tell just by her expression that even she can't focus now."

    "My heart is pounding..."

    "I nervously take another chocolate between my fingers."

    "But this time, Yuri's eyes meet mine."

    show y_cg2_exp3

    y "..."

    "How did it even come to this...?"

    "Yuri doesn't avert her gaze."

    "I notice her chest rising and falling to the rhythm of her breaths."

    "I raise my arm..."

    y "Ah..."

    "Like before, Yuri parts her lips."

    "But...it's different this time."

    hide y_cg2_nochoc

    "I take the chocolate and place it in her mouth."

    "I feel her hot breath on my fingers."

    stop music

    window hide(None)

    scene bg club_day

    window show(None)
    window auto

    show monika 4b zorder 2 at l31

    m "Okay, everyone!"

    mc "Uwa--"

    show yuri 3p zorder 2 at t11

    y "A-Ah!"

    play music t3

    "Yuri jolts back."

    show yuri 3n
    show monika zorder 3 at f31

    m "It's time to share poems!"

    m "[player], you can help Yuri put away the tea stuff, right?"

    show monika zorder 2 at t31

    mc "Y-Yeah...of course."

    show monika zorder 3 at f31

    m "Okay, thanks!"

    show monika zorder 1 at thide
    hide monika

    "The spell is abruptly broken."

    y 4c "I'll..."

    y "I'll take care of the cups..."

    mc "Yeah..."

    show yuri zorder 1 at thide
    hide yuri

    "Yuri picks up the teacups from the floor."

    "I pick up the bag of chocolates."

    "In the end, we hastily clean up without so much as a word between us."

    "I get the feeling this is something neither of us will have the courage to bring up..."

    return

