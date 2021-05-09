label poemresponse_start:

    $ poemsread = 0

    $ skip_transition = False

    label poemresponse_loop:

        $ skip_poem = False

        if renpy.music.get_playing() and not (renpy.music.get_playing() == audio.t5 or renpy.music.get_playing() == audio.t5c):
            $ renpy.music.play(audio.t5, fadeout=1.0, if_changed=True)

        if skip_transition:
            scene bg club_day
        else:
            scene bg club_day
            with wipeleft_scene

        $ skip_transition = False

        if not renpy.music.get_playing():
            play music t5

    label poemresponse_start2:

        $ skip_poem = False

        if persistent.playthrough == 2:
            $ pt = "2"
        else:
            $ pt = ""

        if poemsread == 0:
            $ menutext = "Who should I show my poem to first?"
        else:
            $ menutext = "Who should I show my poem to next?"

        menu:

            "[menutext]"

            "Sayori" if not s_readpoem and persistent.playthrough == 0:
                $ s_readpoem = True

                if chapter == 1 and poemsread == 0:
                    "I'm definitely most comfortable sharing it with Sayori first."

                    "She's my good friend, after all."

                call poemresponse_sayori

            "Natsuki" if not n_readpoem:
                $ n_readpoem = True

                if chapter == 1 and poemsread == 0:
                    "I told Natsuki I was interested in her poems yesterday."

                    "It's probably only fair if I shared mine with her first."

                call poemresponse_natsuki

            "Yuri" if not y_readpoem and not y_ranaway:
                $ y_readpoem = True

                if chapter == 1 and poemsread == 0:
                    "Yuri seems the most experienced, so I should start with her."

                    "I can trust her opinion to be fair."

                call poemresponse_yuri

            "Monika" if not m_readpoem:
                $ m_readpoem = True

                if chapter == 1 and poemsread == 0:
                    "I should start with Monika."

                    "Yesterday she seemed eager to read my poem, and I want her to know I'm putting in effort."

                call poemresponse_monika

        $ poemsread += 1

        if poemsread < 3 or (persistent.playthrough == 0 and poemsread < 4):
            jump poemresponse_loop

    $ s_readpoem = False
    $ n_readpoem = False
    $ y_readpoem = False
    $ m_readpoem = False

    $ poemsread = 0

    return

label poemresponse_sayori:

    scene bg club_day
    show sayori 1a zorder 2 at t11
    with wipeleft_scene

    $ poemopinion = "med"

    if s_poemappeal[chapter - 1] < 0:
        $ poemopinion = "bad"
    elif s_poemappeal[chapter - 1] > 0:
        $ poemopinion = "good"

    $ nextscene = "ch" + pt + str(chapter) + "_s_" + poemopinion

    call expression nextscene

    if not skip_poem:
        $ nextscene = "ch" + pt + str(chapter) + "_s_end"

        call expression nextscene

    return

label poemresponse_natsuki:

    scene bg club_day
    show natsuki 1c zorder 2 at t11
    with wipeleft_scene

    $ poemopinion = "med"

    if n_poemappeal[chapter - 1] < 0:
        $ poemopinion = "bad"
    elif n_poemappeal[chapter - 1] > 0:
        $ poemopinion = "good"

    $ nextscene = "ch" + pt + str(chapter) + "_n_" + poemopinion

    call expression nextscene

    if not skip_poem:
        $ nextscene = "ch" + pt + str(chapter) + "_n_end"

        call expression nextscene

    return

label poemresponse_yuri:

    scene bg club_day
    show yuri 1a zorder 2 at t11
    with wipeleft_scene

    $ poemopinion = "med"

    if y_poemappeal[chapter - 1] < 0:
        $ poemopinion = "bad"
    elif y_poemappeal[chapter - 1] > 0:
        $ poemopinion = "good"

    $ nextscene = "ch" + pt + str(chapter) + "_y_" + poemopinion

    call expression nextscene

    if not skip_poem:
        $ nextscene = "ch" + pt + str(chapter) + "_y_end"

        call expression nextscene

    return

label poemresponse_monika:

    scene bg club_day
    show monika 1a zorder 2 at t11
    with wipeleft_scene

    if m_poemappeal[chapter - 1] < 0:
        $ poemopinion = "bad"
    elif m_poemappeal[chapter - 1] > 0:
        $ poemopinion = "good"

    $ nextscene = "ch" + pt + str(chapter) + "_m_start"

    call expression nextscene
    if not skip_poem:
        $ nextscene = "ch" + pt + str(chapter) + "_m_end"

        call expression nextscene

    return

label ch1_y_end:

    call showpoem (poem_y1, img="yuri 3t")

    y 3t "..."

    y "I...I'm sorry I have such terrible handwriting!"

    mc "What??"

    mc "I wasn't thinking that at all..."

    y 2v "But it took you a long time to read..."

    mc "Ah--"

    mc "Well, I just don't read script very often..."

    mc "I actually think your handwriting is pretty."

    y 2t "Eh?"

    y 2u "That's...a relief..."

    mc "Also, I liked the poem."

    mc "Even though it's short, it was really descriptive."

    y 2t "It wasn't too short?"

    y "I usually write longer poems..."

    mc "Not at all."

    y 1m "I'm...really glad you like it."

    y "I'll be honest..."

    y 1a "Since it's our first time sharing, I wanted to write something a little more mild."

    y "Something easy to digest, I suppose."

    mc "Are you into ghosts, Yuri?"

    y 1m "Huhu."

    y "Actually, the story isn't about a ghost at all, [player]."

    mc "Really?"

    mc "I must have totally missed the point..."

    y 1u "Well, I suppose you did only glance over it, after all..."

    y "But remember that poets often express their own thoughts, feelings, and experiences in their work."

    y 1a "They usually do more than tell a simple story, or paint a picture."

    y "In this case, perhaps the subject of the poem is only being symbolically compared to a ghost."

    y 2l "Lingering in her last remaining place of comfort, unable to let go of the past."

    y "And soon to be left with nothing..."

    mc "...That's a lot more solemn, putting it that way."

    mc "I hadn't even thought of that..."

    mc "That's impressive."

    if poemopinion == "good":
        y 2f "Eh?"

        y 3v "I-It's nothing, really!"

        y "Yours was impressive too, so..."

        mc "Nah..."

        mc "If anything, I could probably learn a thing or two from you."

        y 4a "...You think so?"

        mc "Yeah, of course."

        y "Ah..."

        y 2s "You know..."

        y "I was really nervous about doing all this."

        y "But in the end, I enjoyed it."

        y "I'm going to keep doing my best for you, [player]."

        mc "Ah..."

        mc "Me too."
    else:
        y 1u "It's nothing, really..."

        y "Well...it makes me happy that you think that."

        y 1a "Just remember that it won't be long before you pick up on these things, too."

        mc "Yeah, maybe you're right."

        mc "I guess I'll have to keep trying."

        y "I'm counting on you."

    return

label ch2_y_end:

    call showpoem (poem_y2)

    y 2m "Um..."

    y "I was a little more daring with this one than yesterday's..."

    mc "I can see that."

    mc "It's a lot more metaphorical..."

    "I don't know if it's my fault, but I can't begin to imagine what this poem is about."

    y 1a "That's right."

    y "It's a bit closer to my preferred writing style..."

    y "Using the poem as a canvas to express vivid imagery, and conveying emotions through them."

    mc "Yeah, if I take it at face value, then I can't even figure out what it's supposed to mean..."

    y 2f "Well..."

    y "I think it's something that different people can relate to in their own way."

    y "I wanted to express the way it feels for me to indulge in my more unusual hobbies..."

    y 2v "It's those sorts of things I'm usually forced to keep to myself."

    y "So, I sometimes enjoy writing about them."

    if n_readpoem and (n_poemappeal[0] >= 0 or n_poemappeal[1] >= 0):
        mc "Huh, that's funny..."

        y 2e "...?"

        mc "Didn't Natsuki also write something about that?"

        mc "About someone being ridiculed for a strange interest?"

        y 2h "Eh?"

        y "She...she did?"

        mc "Yeah..."

        mc "She was talking about how it doesn't matter what you're into as long as you're not hurting anybody."

        y 3r "She--She's right!"

        y 3o "Ah--I mean..."

        y "Does she really feel that way...?"

        mc "Yeah."

        mc "Sounds like you two have that in common..."

        y 3h "That's...well, that's interesting..."

        y "To me, she seemed like the kind of person who would make fun of my hobbies..."

        y "But I suppose that's my fault for judging, isn't it...?"

        y 3p "Ah-- Please don't tell her I said that!"

        mc "Ahaha. Don't worry, I have no reason to."

        y 1l "Okay..."

        y 1a "Well, thank you for sharing it with me."
    else:
        mc "Why do you keep them to yourself?"

        y 3v "Be...Because..."

        y "They're embarrassing..."

        y "And people would make fun of me."

        y "Don't you have anything like that, [player]?"

        mc "Well..."

        mc "Yeah, I guess I do..."

        y 2h "I feel like everyone has a little something like that."

        y "The best we can do is respect each other and our individualities."

        y "Even if it's difficult sometimes, and some things make us uncomfortable..."

    y 1a "After all, if I hadn't learned to embrace my own weirdness, I would probably hate myself."

    y 2u "I-I might be ranting a little bit now..."

    y "...But I'm glad that you're a good listener."

    if y_appeal >= 2:
        y 2s "You're good at a lot of things..."

        y "Writing, listening..."

        y 2u "There really aren't many people like you, [player]..."

        mc "Th-That's exaggerating a little bit..."

        y 2v "It's just...how I feel."

        y "I never thought I would feel so comfortable sharing my writing..."

        y 2s "But now, I almost feel like I look forward to it..."

        y 2m "It's just...a really nice feeling."

        y "And you're to thank for that."

        mc "It's...it's nothing, really..."

        "Yuri smiles sincerely at me."

        "For just a moment, her timidness seems to disappear."

    return

label ch3_y_end:

    $ y_read3 = True

    if y_appeal >= 3:
        jump ch3_y_end_special

    call showpoem (poem_y3, img="yuri 2v")

    y "Um..."

    y "I'm aware that the beach is kind of an inane thing to write about."

    y "But I did my best to take a metaphorical approach to it."

    if not n_read3 or n_appeal >= 3:
        mc "You say that like you didn't even want to write about it..."

        y 2e "Oh, you haven't heard...?"

        y 2h "After yesterday, Natsuki and I...well..."

        y "It was...amusing that we wrote about something similar in such different ways."

        y "So, Natsuki wanted us to write about the same topic as each other again."

        if n_readpoem:
            if not n_read3:
                mc "I see..."

                "Natsuki didn't even let me read her poem, so I don't have much to contribute."
            else:
                mc "I see..."

                "Something tells me the poem Natsuki showed me isn't the one she plans on sharing with everyone else..."

                "Of course, I choose not to mention that to Yuri."
    else:
        mc "Yeah, Natsuki already told me about it."

        y 3t "S-She did...?"

        y "She didn't say anything weird, did she?"

        y "She just wanted us to write about the same topic again..."

    y 2f "I suppose to better compare the differences in our writing styles...or thought processes."

    y 2w "Anyway, it was her idea...!"

    y "Knowing her, it's no surprise that she'd want to do something like that."

    y "She probably just wants to show off."

    y 2v "It's not like I have a particular interest in her writing style..."

    y "I just went with her request."

    y "But..."

    y 1s "Well, I suppose it's not so bad to write about something simple on occasion."

    y 1m "It can be refreshing, you know?"

    y "It's good for me to calm my thoughts once in a while."

    mc "Yeah...I think I agree."

    mc "Thanks for sharing."

    return

label ch3_y_end_special:

    call showpoem (poem_y3b, img="yuri 4b")

    "Finishing the poem, I start to hand it back to Yuri."

    "But instead of taking it from me, she looks away."

    y "..."

    y "Do you...dislike it?"

    mc "Ah--no, of course not."

    mc "I just...don't really know how I should respond."

    "Despite Yuri's poems usually being cryptic, it wasn't hard to figure out what this one was about."

    if n_read3:
        "Also, this clearly isn't the poem that Natsuki said she wrote about..."

        "...Meaning I'm probably the only one she's showing this to."

    y 2v "I-I don't know if I'll be able to explain this one..."

    mc "That's fine."

    mc "I understand this one."

    y 4c "..."

    "Yuri is having an even harder time speaking than usual."

    mc "Does this one...mean a lot to you?"

    "Yuri nods."

    mc "I'm not really good with words, but..."

    mc "I'm happy that you shared it with me."

    mc "So, thank you."

    mc "And I hope we keep spending time together."

    show yuri 4e

    "Despite my inability to make eye contact, I see a faint smile emerge on Yuri's lips."

    "I once again try to hand the poem back to her."

    show yuri 4a

    "But instead, Yuri gently takes my hands and pushes them back toward me."

    "I hesitate in response to her warm touch."

    y 1v "You can..."

    y "Um..."

    y "The poem is..."

    "Once again, Yuri fails to form a complete sentence."

    mc "You mean I can keep it?"

    "Yuri nods."

    mc "I'd love to."

    show yuri 1u

    "Again, Yuri faintly smiles, as if she doesn't want me to notice."

    y "You always..."

    y "You always...make me feel nice."

    y "I know I'm not good with people, but..."

    y "I hope that...I can return the favor sometimes."

    mc "Yeah."

    mc "Don't worry."

    mc "I think you do a good job."

    "Yuri finally turns back toward me."

    y 1s "I guess...we should move on before Monika says something."

    y "But I'm sure we can talk again later..."

    mc "Yeah."

    mc "I'm sure we will."

    "With that, Yuri timidly smiles at me, and I return to my seat so I can put her poem away."

    return

label ch1_n_end:

    call showpoem (poem_n1, img="natsuki 2s")

    n 2q "Yeah..."

    n "I told you that you weren't gonna like it."

    mc "I like it."

    n 2h "What?"

    n "Just be honest!"

    mc "I am."

    mc "Why are you so convinced that I wouldn't like it?"

    n 5w "Well--"

    n "Because!"

    n "Everyone in high school thinks that writing has to be all sophisticated and stuff..."

    n 5q "So people don't even take my writing seriously."

    mc "But isn't the point of poems for people to express themselves?"

    mc "Your writing style wouldn't make your message any less valid."

    n 1k "Yes! Exactly!"

    n "I like when it's easy to read, but it hits you hard."

    n 1c "Like in this poem."

    n "Seeing everyone around you do great things can be really disheartening..."

    n "So I decided to write about it."

    mc "Yeah, I understand."

    n 2a "But the other nice thing about simple writing is that it puts more weight on the wordplay."

    n "Like I set up for a rhyme at the end, but then made it fall flat on purpose."

    n "It helps bring out the feeling in the last line."

    mc "So you did..."

    mc "I guess more went into it than I realized."

    n 4y "That's what it means to be a pro!"

    n "I'm glad you learned something."

    n "Didn't expect that from the youngest one here, did you?"

    mc "Yeah...guess not."

    "I decide to humor her with that last comment."

    "I don't really care how old everyone is, but if Natsuki is feeling proud then I won't take that away from her."

    return

label ch2_n_end:

    call showpoem (poem_n2)

    n 2a "Not bad, right?"

    mc "It's quite a bit longer than yesterday's."

    n 2w "Yesterday's was way too short..."

    n "I was just warming up!"

    n 2c "I hope you didn't think that was the best I could do."

    mc "No, of course not..."

    n 2a "Anyway, the message is pretty straightforward in this poem."

    n "I doubt I have to explain it."

    n 2c "Sometimes you can explain complicated issues with much simpler analogies..."

    n "And it helps people realize how stupid they're being."

    n 2g "Like, anyone would agree that the subject of this poem is an ignorant jerk..."

    mc "Do you know people like that?"

    n 2c "Of course. It's about how everyone thinks my--"

    n 5w "...That doesn't matter! It can be about anything!"

    n 5h "I wrote it to be easy to relate to..."

    n "Everyone has some kind of weird hobby, or a guilty pleasure."

    n 5q "Something that you're afraid if people find out, they'd make fun of you or think less of you."

    n 1e "...But that just makes people stupid!"

    n "Who cares what someone likes, as long as they're not hurting anyone, and it makes them happy?"

    n 1q "I think people really need to learn to respect others for liking weird things..."

    if y_readpoem and (y_poemappeal[0] >= 0 or y_poemappeal[1] >= 0):
        mc "Huh, that's funny..."

        mc "Yuri wrote about something similar today."

        n 1h "Huh?"

        n "Did you say Yuri?"

        mc "Yeah..."

        mc "She said her poem was about an unusual hobby of hers."

        mc "I didn't really get it, but she said something similar to you..."

        mc "That people shouldn't make each other feel insecure about those things."

        n 1q "Really?"

        n "Well..."

        n 1t "I mean, Yuri's pretty weird, so I wouldn't doubt that she has some weird hobbies..."

        n "...Not that there's anything wrong with that!"

        n 1u "Uu..."

        n "It's not like...I would judge her or anything..."

        "Natsuki has trouble finding words."

        n 1q "I-I guess I should try not to be so mean to her..."

        n "If she feels insecure about her weird behaviors and stuff..."

        n "I mean, I always hate people who make me feel insecure..."

        n 1w "And Yuri made me feel insecure yesterday!"

        n 1s "But the way you put it, it sounds like she's learned her lesson..."

        mc "Well, I would say so."

        mc "Even if her writing style is really different, I'm sure she'll appreciate the message in your poem."
    else:
        mc "Well, you're definitely right."

        mc "At least, I can relate to that."

        mc "And I'm sure a lot of other people can, too."

    if n_appeal >= 2:
        n 4h "You know..."

        n "I'm glad that you can appreciate this kind of writing..."

        n 4q "I mean...I know I was talking about that yesterday."

        n "But I've been...well, I've been enjoying sharing my writing with you, so..."

        n 4w "...So consider yourself lucky, okay?"

        mc "Ahaha."

        mc "Well, thanks for being honest."

        n 1n "What's that supposed to mean?"

        n "I'm always honest!"

        n 12b "Jeez..."

        n "Just look forward to tomorrow too, okay?"

        mc "Alright, I will."
    else:
        n 4c "It's what I do best, after all!"

        n "I don't like writing unless there's a good message to take away from it."

        n "Like, conveying emotions is important..."

        n "But I want to make people think, not just feel."

        n 4b "Remember that!"

        n "I'm gonna write a good one for tomorrow, too, so look forward to it."

    return

label ch3_n_end:

    $ n_read3 = True

    if n_appeal >= 3:
        jump ch3_n_end_special

    call showpoem (poem_n3)

    n 2a "Yeah..."

    n "I felt like I kept writing about negative things, so I wanted to write something with a nice message for once."

    n 2z "Besides...the beach is awesome!"

    n 2j "Kinda hard to write anything negative about the beach."

    if not y_read3 or y_appeal >= 3:
        mc "So you decided to write about the beach first, and then came up with the message later?"

        n 2c "Yeah, well..."

        n "It's only because of what happened yesterday."

        n 5q "I mean, after Yuri and I realized we kind of wrote about the same thing..."

        n "She wanted to pick a topic and have us both write about it, or whatever."

        if y_readpoem:
            if not y_read3:
                mc "I see..."

                "I don't really have much to contribute here, since I didn't actually read Yuri's poem..."
            else:
                mc "I see..."

                "Something tells me the poem Yuri showed me isn't the one she plans on sharing with everyone else..."


                "Of course, I choose not to mention that to Natsuki."
    else:
        mc "Well, Yuri's take on it was a little more solemn."

        n 5h "Well, that's--"

        n 42c "Jeez...she better not have said anything bad about mine!"

        n "After all, she was the one who wanted us to write about the same topic."

    n 1s "Ugh...you can really see her doing that, too."

    n "Making us write about a simple topic, then trying to impress me by coming up with something all fancy."

    n 1w "Well, it's not like I care."

    n "I just did it anyway."

    n 1q "I mean, I guess mine ended up being kind of metaphorical too..."

    n "...But there's nothing wrong with doing that once in a while!"

    n "At the very least, it was good practice."

    return

label ch3_n_end_special:

    call showpoem (poem_n3b)

    n 1q "..."

    n "...Why are you looking at me like that?"

    n "If you don't like it, then just say it."

    n 1u "I won't...get mad."

    mc "No, it's not that I don't like it...!"

    mc "It was just...a little surprising to read."

    if y_read3:
        "This clearly isn't the poem that Yuri told me she had written..."

        "...Meaning I'm probably the only one she's showing this to."

    mc "Er...I guess I'm not used to hearing such nice things coming from you..."

    n 1h "D-Don't just say that!"

    n 1n "Dummy..."

    n "What do you think...the point of writing is?"

    n 1u "Expressing things that you can't just say..."

    mc "Yeah...I understand."

    mc "I'm sorry for missing the point sometimes."

    mc "I always mean well..."

    mc "And...I'm happy that you showed this to me."

    mc "I liked it."

    n 1h "Well...yeah..."

    n 1q "I'm...I'm a pro, so..."

    "Natsuki mumbles, completely failing to sound confident like she usually does."

    n "Just..."

    n 12c "Remember that...I can think these things sometimes, too!"

    n "You know, when you're nice to me, it's..."

    n 12a "..."

    n "...Meaningful."

    mc "Ah...I'm glad."

    "Sensing Natsuki is satisfied, I start to hand the poem back to her."

    "But as I do so, Natsuki takes my hands and pushes them back away."

    "Her small, soft hands surprise me with their assertion."

    n 12b "I don't want it."

    mc "Eh...?"

    mc "Why not?"

    n 12c "I just don't!"

    n "Jeez..."

    "I realize what Natsuki is doing."

    "Unable to be honest, she's trying to give me the poem in a roundabout way."

    mc "Well...in that case, I'm going to keep it."

    "Instead of teasing her, I choose to go along with it."

    n 1t "...Good."

    n "If you didn't, I would..."

    n "..."

    n 1h "Never mind..."

    n 1q "Just...I'm glad that you want it."

    "Natsuki backpedals on her words and leaves it at that."

    "Despite her best efforts to hide her expression, I can see her faintly smiling to herself."

    n "That's all for now, so..."

    n 1s "Go put it away before someone sees it, okay?"

    mc "Ah...yeah."

    mc "I'll go do that."

    "With that, I return to my seat so that I can put away Natsuki's poem."

    return

label ch1_s_end:

    call showpoem (poem_s1)

    mc "Sayori..."

    mc "This is just a guess, but..."

    mc "Did you wait until this morning to write this?"

    s 4h "No!"

    s 4l "J-Just a little bit!"

    mc "You can't answer 'just a little bit' to a yes or no question..."

    s 5b "I forgot to do it last night..."

    mc "Well, at least that makes me feel a little better about myself..."

    s 1h "Don't be mean!"

    s "I still tried my best..."

    mc "Ah, yeah..."

    mc "I didn't mean to say that it was a bad poem."

    mc "It came out nice...or, how should I put it..."

    mc "It sounds just like you."

    s 1d "Really?"

    mc "Yeah."

    mc "Especially that last line..."

    s 4r "I made eggs and toast!"

    mc "Even though you were late to school...?"

    s 5d "It's bad to skip breakfast!"

    s "I get all cranky..."

    mc "Well, I guess there's no point in arguing..."

    mc "Anyway, thanks for showing me."

    s 1q "Ehehe~"

    s "This was so much fun."

    s "Monika's the best!"

    mc "Ah...yeah."

    s "But next time, I won't forget."

    s 4x "And I'm gonna write the best poem ever!"

    mc "Well, I guess I look forward to it."

    return

label ch2_s_end:

    call showpoem (poem_s2)

    mc "Holy crap..."

    mc "Sayori, did you really write this?"

    s 2j "Of course I did!"

    s "Didn't I tell you yesterday I was gonna write the best poem ever?"

    mc "Yeah, but..."

    mc "I mean, I didn't expect something like this, coming from you."

    s 4x "Monika taught me a whole lot!"

    s "And I've been really in touch with my feelings recently..."


    mc "I see that..."

    mc "It's almost kind of creepy."

    s 1b "Creepy...?"

    mc "Well, not exactly..."

    mc "Maybe because I'm so used to you being cheerful..."

    mc "...Well, never mind."

    mc "I'm thinking too hard about it."

    mc "The point is, it came out good, so you should be proud of it."

    s 1y "Aw, thanks~"

    s "I feel like..."

    s "I feel like I was meant to express myself this way."

    s "It even helps me understand my own feelings a little bit better..."

    s 1a "Writing is like magic!"

    mc "You've gotten pretty passionate about this, huh?"

    mc "I hope you keep it up."

    s 4r "Yeah!"

    s "Writing's the best!"


    s "I'm gonna keep writing until I die!"

    mc "Ahaha...don't get ahead of yourself."

    "Sayori's always had a habit of getting obsessed with something, before dropping it no more than a week later."

    "I wonder if this is one of those times?"

    "But seeing the passion in her eyes makes it hard for me to be pessimistic."

    return

label ch3_s_end:

    return

label ch1_m_end:

    call showpoem (poem_m1)

label ch1_m_end2:

    m 1a "So...what do you think?"

    mc "Hmm...it's very...freeform, if that's what you call it."

    mc "Sorry, I'm not really the right person to ask for feedback..."

    m 2e "Ahaha. It's okay."

    m 2b "Yeah, that kind of style has gotten pretty popular nowadays."

    m "That is, a lot of poems have been putting emphasis on the timing between words and lines."

    m 2a "When performed out loud, it can be really powerful."

    mc "What was the inspiration behind this one?"

    m "Ah..."

    m 3d "Well, I'm not sure if I know how to put it..."

    m 3a "I guess you could say that I had some kind of epiphany recently."

    m "It's been influencing my poems a bit."

    mc "An epiphany?"

    m 1a "Yeah...something like that."

    m "I'm kind of nervous to talk about deep stuff like that, because it's kind of coming on strongly..."

    m "Maybe after everyone is better friends with each other."

    m 1j "Anyway..."

    m 3b "Here's Monika's Writing Tip of the Day!"

    m "Sometimes when you're writing a poem - or a story - your brain gets too fixated on a specific point..."

    m "If you try so hard to make it perfect, then you'll never make any progress."

    m "Just force yourself to get something down on the paper, and tidy it up later!"

    m "Another way to think about it is this:"

    m "If you keep your pen in the same spot for too long, you'll just get a big dark puddle of ink."

    m "So just move your hand, and go with the flow!"

    m 3k "...That's my advice for today!"

    m "Thanks for listening~"

    return

label ch2_m_end:

    call showpoem (poem_m2)

    mc "Hm..."

    mc "It's even more abstract than your last one, huh?"

    m 5 "Ahaha..."

    m "I guess it's just the way I write..."

    m "I'm sorry if you don't like it."

    mc "No, I never said that."

    mc "It's just a kind of thing I've never really seen before, I guess."

    m 2a "I kind of like playing with my space on the paper..."

    m "Choosing where and how to space your words can totally change the mood of the poem."

    m 2b "It's almost like magic."

    m "The way I wrote the lines really short makes it feel like they're trying to speak over the noise."

    mc "I see..."

    mc "It's still hard for me to tell what it's about, though."

    m 2k "Ahaha."

    m 4a "Sometimes asking what a poem is about isn't the right question."

    m "A poem can be as abstract as a physical expression of a feeling."

    m "Or a conversation with the reader."

    m "So putting it that way, not every poem is {i}about{/i} something."

    m "Anyway..."

    m 3b "Here's Monika's Writing Tip of the Day!"

    m "Sometimes you'll find yourself facing a difficult decision..."

    m "When that happens, don't forget to save your game!"

    m "You never know when you might change your mind..."

    m "...or when something unexpected may happen!"

    m 3d "Wait...is this tip even about writing?"

    m 3k "What am I even talking about?"

    m "Ahaha!"

    m 3b "...That's my advice for today!"

    m "Thanks for listening~"

    return

label ch3_m_end:

    call showpoem (poem_m3)

    m 1a "You know..."

    m "I feel like learning and looking for answers are the sorts of things that give life meaning."

    m 1e "Not to get too philosophical or anything..."

    m 1a "But it was kind of on my mind, so that's what I wrote about."

    mc "I see..."

    mc "I never really put much thought into it."

    m 1d "In a way, it's almost paradoxical."

    m "Because if we had all the answers, wouldn't the world start to lose its meaning?"

    mc "You know, there's one thing I noticed..."

    mc "It seems like everyone in the club prefers writing about things that are more sad than happy."

    m 1k "Ahaha. Are you surprised?"

    m 1a "I mean, if everything was okay..."

    m "We wouldn't really have anything to write about, would we?"

    m "Humans aren't two-dimensional creatures."

    m "I think you'd know that better than anyone."

    mc "You mean one-dimensional...?"

    m 1l "Ah...yeah, that!"

    m 1a "Anyway..."

    m 3b "Here's Monika's Writing Tip of the Day!"

    m "Are you ever too shy to share your writing because you're afraid it's not that good?"

    m "It can be really disheartening to get a lukewarm response to something you put so much into."

    m "But if you find other people who enjoy writing, then sharing becomes a lot easier!"

    m "Because instead of just telling you that your writing is good, or okay, or bad..."

    m "They'll want to focus more on everything that went into it, and the things you can work on."

    m "It's much more encouraging that way, and it will make you want to continue improving."

    m "It's almost like having your own little Literature Club, don't you think?"

    m 3k "...That's my advice for today!"

    m "Thanks for listening~"

    return

label ch1_n_bad:

    n "..."

    mc "...?"

    if persistent.playthrough == 2 and renpy.random.randint(0, 2) == 0:
        $ currentpos = get_pos()

        stop music

        $ pause(2.0)

        play sound "sfx/stab.ogg"

        show n_blackeyes zorder 3 at i11
        show n_eye zorder 3:
            subpixel True
            pos (660,250) xanchor 0.5 yanchor 0.5 zoom 0.8
            parallel:
                linear 2.0 rotate 720
            parallel:
                linear 2.0 xpos 1680
            parallel:
                easein 0.25 ypos 180
                easeout 1.0 ypos 1280
        show n_eye as n_eye2 zorder 3:
            subpixel True
            pos (580,260) xanchor 0.5 yanchor 0.5 zoom 0.8 rotate 180
            parallel:
                linear 2.0 rotate -560
            parallel:
                linear 2.0 xpos -440
            parallel:
                easein 0.10 ypos 240
                easeout 1.0 ypos 1280
        show blood zorder 3:
            pos (645,255)
        show blood as blood2 zorder 3:
            pos (575,260)

        $ pause(0.75)

        hide n_blackeyes
        hide n_eye
        hide n_eye2
        hide blood
        hide blood2

        stop sound

        play music "<from " + str(currentpos) + " loop 4.444>bgm/5.ogg"

    n 2b "[player], if you're not going to take this club seriously then go home."

    mc "W-What??"

    mc "Harsh..."

    n 42c "What, you expect me to believe that you actually put effort into this?"

    n "Do you think I'm stupid?"

    mc "I'm not a writer!"

    mc "Maybe it's not very good, but yeah, I did put in effort."

    mc "We all start somewhere, right?"

    mc "If you're still proud of the first poem {i}you{/i} ever wrote, then I'd like to read it."

    n 1o "!!"

    mc "Painful to think about?"

    n 1r "..."

    n 5q "Fine."

    n "Well, sorry."

    n 5c "You'll get better, anyway."

    n "I'd tell you what to improve, but you're better off just trying again."

    mc "Fair enough..."

    mc "Well, to each their own, I guess."

    n 5q "Anyway, I guess I gotta share mine now..."

    n "Knowing you, you'll probably think it's stupid."

    return

label ch1_n_med:

    n "..."

    mc "...?"

    n 2k "...Well, it's about what I expected from someone like you."

    mc "That's a little blunt..."

    n 2c "Well, excuse me."

    n "It's not like I said it was bad."

    n "It just didn't evoke any emotions."

    mc "So basically, it's not cute enough for your tastes?"

    n 4f "Do you want to get smacked?"

    mc "I'll pass..."

    n 42b "Sigh..."

    n 42c "Well anyway, I guess I need to show you mine."

    n 4q "Not that you'll like it."

    return

label ch1_n_good:

    n "..."

    mc "...?"

    n 1t "...Okay, well let's start with the things I don't like!"

    n "First of all, um..."

    mc "..."

    "Natsuki re-reads my poem."

    n 4c "N-Never mind. I don't feel like giving you my opinion."

    mc "Eh? Then what's the point of sharing in the first place?"

    mc "I wrote this when I could have been doing other things."

    n 4r "Uu..."

    mc "In fact, remember how I said I wanted to read your poems?"

    mc "That's what I had in mind when writing this."

    mc "I want to help you feel comfortable enough to share yours."

    mc "Like Monika said."

    n 4x "Uuuu...!"

    n 1h "Well I would be more comfortable sharing my poem if yours was really bad!"

    n 1w "You were supposed to show me some dumb poem and make me go 'Hah, well it's not that great but let me show you what real literature looks like!'"

    n 1h "And you went and ruined it!"

    n "I hope you're happy!"

    mc "..."

    mc "...So, in other words, you're saying you liked it?"

    n 1o "Urk--"

    "Natsuki's retort gets caught in her throat."

    n 1x "Uuuuuuuuu...You're so...!"

    n "You just...you...don't understand anything, do you?"

    n 5q "I already told you that, you don't have to go announcing it to the world like you're all self-important!"

    mc "Pretty sure you never actually said that..."

    "I say that mostly to myself."

    "Natsuki must really hate me or something."

    "I can't figure out if it's a win or a loss that she liked my poem."

    mc "In any case... You still need to show me yours, right?"

    n 5s "Gr... Fine, I guess."

    n "Only because Monika will make me if I don't."

    return

label ch2_n_bad:

    if n_poemappeal[0] < 0:
        n "...Hm."

        n 2k "Well, I can admit that it's better than the last one."

        n "It's nice to see that you're putting in some effort."

        mc "That's good..."

        n 2c "But I still don't like this at all."

        n "It's trying too hard to be serious."

        mc "Eh? What do you mean by that?"

        label ch2_n_bad_sharedwithch3:

            n 4c "Poems don't need to be all deep-sounding to express something."

            n "It's going to just sound like you're forcing it unless you really don't suck at it."

            n 4w "Honestly... Don't bother trying to write poems like this until you're on Yuri's level--"

            show natsuki 4o

            "Natsuki stops short all of a sudden."

            n 1o "D-Don't...tell me..."

            mc "Eh?"

            n "You're not...you're not just trying to impress Yuri, are you?!"

            mc "W-What are you talking about?? And keep your voice down...!"

            n 1x "You know Yuri would love this kind of...this angsty.......!!"

            mc "Just because she's a talented writer doesn't mean...I-I mean..."

            n 1o "Uu....!!"

            "Looks like I'm in trouble."

            "I somehow struck a nerve, though what I did is beyond me."

            n 1c "I am so done with you."

            "Natsuki shoves the poem I handed her back over to me."

            n 5w "Take your stupid poem. If you wrote it for someone else, just don't show it to me!"

            mc "Ouch..."

            "This is what I get for letting a younger girl step into my business."

            "Unless I was a mind reader, I was destined to be in a world of pain from the start."

            "At least Natsuki wasn't really the girl I was trying to impress in the first place..."

            $ skip_poem = True

            return
    else:
        n 1k "...Hm."

        n "I liked your last one better."

        mc "Eh? Really?"

        n 2c "Well yeah. I can tell you were a little more daring with this one."

        n "But you're really not good enough for that yet. It fell flat."

        mc "That may be true, but I just wanted to try something different."

        mc "I'm still figuring this all out."

        n 2k "I mean, I always like poems that aren't trying too hard."

        n 2q "I hate when people try to sound fancy or add more meaning just by using annoying and complicated language."

        n 4b "Just make it simple, cute, and to the point!"

        n 4y "Yuri's head over heels for all this cryptic nonsense, but I see right through that BS. Hah!"

        n 42a "Making your reader look so hard for all this deep meaning is just an excuse to have no meaning at all."

        mc "I guess that's one way to look at it."

        n 2d "Well, everyone has their own opinion."

        n "But my opinion is the best opinion. I'm sure you've figured that out already."

        mc "Er..."

        n 2a "Anyway, here's my poem. Maybe you'll learn something."

        return

label ch2_n_med:

    if n_poemappeal[0] < 0:
        n "...Hm."

        n 2k "Well, I can admit that it's better than the last one."

        n "It's nice to see that you're putting in some effort."

        mc "That's good..."

        label ch2_n_med_shared:

            n 2c "Come to think of it, this kind of reminds me of Sayori's poem from yesterday..."

            mc "Eh? You think so?"

            n 2j "Yeah. Well I guess if you've been friends with her for so long, you might be on the same wavelength."

            n 2k "But you never really struck me as her type."

            mc "Sayori has a 'type' all of a sudden...?"

            n 42c "Well, I don't know! But honestly, how can someone so...er, fluffy...spend so much time with someone like you?"

            n "It's like she's dragging around a dead weight."

            mc "Uug... That was a little unnecessary..."

            mc "But think of it this way. If it weren't for me, she would probably just fly away like letting go of a balloon."

            mc "You could say we each take care of each other in our own way."

            n 2q "Whatever it is, I don't get it..."

            n "...Oh, yeah, I guess I'm supposed to show you my poem."

            n "Here."

            return
    elif n_poemappeal[0] == 0:
        n "...Hm."

        n 2k "Well, it's not really any worse than your last one."

        n "But I can't really say it's any better, either."

        mc "Phew..."

        n 2c "Huh? 'Phew' what?"

        mc "Ah... Well anything that isn't a trainwreck, I'll take as a win."

        mc "And I get the feeling you're probably the most critical."

        n 1p "H-Hey! What makes you--"

        n 1q "{i}(Wait, maybe that was a compliment...?){/i}"

        n 4y "A-Ahah! Glad to see someone recognizes my experience!"

        n "Well then, keep practicing and maybe you'll be as good as me someday!"

        mc "That's...uh..."

        "Something tells me Natsuki completely missed the point."

        jump ch2_n_med_shared
    else:
        n "...Hm."

        n 2c "Well, it's not terrible."

        n "But it's pretty disappointing after your last one."

        n 2s "Then again, if this one was as good as your last one, I would be completely pissed."

        mc "Well, I guess I wanted to try something a little different this time."

        n 2c "Fair enough. You're still new to this, so I wouldn't expect you to find your style right away."

        jump ch2_n_med_shared

label ch2_n_good:

    if n_poemappeal[0] != 1:
        n 1h "..."

        "Natsuki reads my poem."

        "She keeps glancing at me, then back at the poem."

        "By now, she must have read it more than once."

        n 1q "...Aren't you supposed to be bad at this?"

        mc "...Is that a compliment?"

        n 1o "N-No! I mean... You know..."

        "Natsuki struggles to find the words she wants."

        n 5w "I just...expected a lot less after what you showed me yesterday."

        n "That's all."

        mc "Well, I guess I just got lucky with this one."

        n 4t "Y-Yeah!! Exactly!"

        n "You just got lucky, you know?"

        n 4y "Don't get used to it."

        n "You won't always manage to write poems this cute. I mean--!"

        n 1p "I mean well-written! No, I mean--"

        mc "Ah, so that's how it is. My poem is cute?"

        n 1v "No! Why are you smiling?! It's not like I like cute things!"

        "Natsuki shoves my poem back towards me."

        n 4w "H-Huh! Reading it again, I decided that it's not so great after all."

        n "It's too cute and doki-doki."

        n 4t "It would only impress...you know, girls...who like those kinds of things."

        n "Ahaha!"

        "For some reason, Natsuki is incredibly easy to see through."

        n 1w "Well, anyway...!"

        n 1h "You're gonna read mine now, right?"

        n "Judging by your tastes, you'll probably like it a lot."

        n 2q "You'll probably learn something, too. Don't forget who the {i}real{/i} pro is."

        return
    else:
        label ch2_n_good_sharedwithch3:

            n 1n "..."

            "Natsuki reads my poem."

            "She keeps glancing at me, then back at the poem."

            "By now, she must have read it more than once."

            n 1u "Rrgh..."

            mc "...?"

            mc "Is it that bad?"

            n 1r "No! No, it's not!"

            n "It's good. It's really good, okay?!"

            n 5w "There, I said it!"

            n "Ugh, this wasn't supposed to happen at all...!"

            n 5s "Why can't you just be bad at this?"

            n "My poems are supposed to impress {i}you{/i}, not the other way around!"

            mc "You're trying to impress me?"

            n 12c "Obviously! You think I'd let you enjoy Yuri's writing more than mine?"

            n "Give me a break."

            mc "Well..."

            mc "In that case, what's the problem with me trying to impress you?"

            n 1e "I'll tell you! You--"

            n 1p "--"

            "Natsuki's face freezes, like she just realized something."

            n "Y-Y-You..."

            n "You're trying to...impress {i}me?{/i}"

            show natsuki 1q

            "Natsuki vigorously scans her eyes over my poem one more time."

            "Then, the poem slips out of her hands and flutters to the floor."

            n 1p "I...have to use the bathroom!"

            show natsuki at lhide
            hide natsuki

            "Red-faced, Natsuki quickly walks out of the room."

            show monika 1d zorder 2 at t11

            m "Hey, [player]..."

            m "Did you do something to Natsuki?"

            m "I just saw her rush out like that..."

            m 2g "You didn't do anything terrible, did you?"

            mc "N-No!"

            mc "I just told her that--"

            "My voice gets caught in my throat."

            "There's no way I could tell Monika that I'm trying to impress Natsuki."

            m 2d "Hmm?"

            "Monika sees the poem lying on the floor and swiftly picks it up."

            if m_readpoem:
                "She skims over it a second time, her smile not fading from her face."

                m 2a "I see."
                m "At first I just thought you liked her writing style..."

                m "But you wrote this {i}for{/i} Natsuki, didn't you?"
            else:

                $ n_poemearly = True

                "She reads through it, her smile not fading from her face."

                m 2a "I see."

                m "You wrote this for Natsuki, didn't you?"

            mc "I-I mean..."

            mc "Not really..."

            m 2d "In fact, didn't she like your poem a lot the other day, too?"

            m "I'm surprised you know her taste so well already."

            m 4a "Are you sure you're not cheating, [player]?"

            mc "Cheating...?"

            mc "What do you mean by that?"

            m 5a "Never mind, I'm just kidding. Ahaha!"

            "I didn't understand Monika's joke at all."

            m "Anyway..."

            m 1a "How do you think Natsuki feels about you?"

            m "Oh, you don't need to answer that."

            m "It was just something for you to think about."

            show monika zorder 2 at t22
            show natsuki 4e at l21

            n "Hey!"

            "Natsuki comes up and snatches the poem out of Monika's hands."

            "Neither of us had noticed her reenter the classroom."

            show natsuki zorder 3 at f21

            n "Did you read this, Monika?"

            show natsuki zorder 2 at t21
            show monika zorder 3 at f22

            m 1j "Of course! I liked it!"

            show monika 1a zorder 2 at t22
            show natsuki zorder 3 at f21

            n 1r "Ugh..."

            n "You should really stop reading things that aren't for you, you know."

            n "You have a bad habit of doing that."

            show natsuki zorder 2 at t21
            show monika zorder 3 at f22

            m 1d "Eh?"

            m "But [player] wrote this poem."

            m 1a "And we're supposed to share with everyone, right?"

            show monika zorder 2 at t22
            show natsuki zorder 3 at f21

            n 1x "Uu--"

            "Natsuki freezes."

            "She apparently forgot that my poem is technically for everyone to read."

            n 42c "Okay, well, I think [player] is done sharing this poem with everyone."

            n "It's not like anyone would want to read this anyway."

            n 4h "In fact, I'm just going to hold onto this."

            show natsuki zorder 2 at t21
            show monika zorder 3 at f22

            m 5 "If you insist~"

            show monika zorder 2 at t22
            show natsuki zorder 3 at f21

            n 1i "What?"

            n "Why are you looking at me like that??"

            show natsuki zorder 2 at t21
            show monika zorder 3 at f22

            m "Like what?"

            show monika zorder 2 at t22
            show natsuki zorder 3 at f21

            n 12b "Ugh..."

            n "Never mind."

            if s_readpoem and y_readpoem:
                "Well, I guess Natsuki has my poem now."

                "Not that I really planned on keeping it."
            else:
                $ unfairto = "Sayori"

                if s_readpoem:
                    $ unfairto = "Yuri"

                show natsuki zorder 2 at t21

                mc "Ah, Natsuki..."

                mc "I'll give you the poem, but that's still not very fair to [unfairto]..."

                mc "...She hasn't gotten to read it yet."

                show natsuki zorder 3 at f21

                n 2q "So what?"

                show natsuki zorder 2 at t21
                show monika zorder 3 at f22

                m 2a "Well... I guess [player] is right, Natsuki..."

                m "It's not fair if you don't let everyone finish reading it."

                show monika zorder 2 at t22
                show natsuki zorder 3 at f21

                n "..."

                n 2h "...Fine."

                "Natsuki returns my poem."

                n "It's not like she's going to like it, though."

            show monika zorder 1 at thide
            show natsuki zorder 2 at t11
            hide monika

            n 2h "Anyway, read my poem now."

            n 4h "And no, I won't let you keep it."

            n "This is my only copy."

            return

label ch3_n_bad:

    if n_poemappeal[0] < 0 and n_poemappeal[1] < 0:
        label ch3_n_bad12_shared:

            n 5x "Yeah, no thanks."

            mc "Eh? You didn't even--"

            n 5w "{i}Next!{/i}"

            $ skip_poem = True

            return
    elif n_poemappeal[0] < 0 or n_poemappeal[1] < 0:
        n "..."

        n 2c "...Meh."

        n "I guess you really haven't learned anything after all."

        n "Honestly, I don't know why I got my hopes up in the first place."

        mc "What? I didn't think this one was that bad..."

        mc "What did I do wrong?"

        jump ch2_n_bad_sharedwithch3
    else:
        n "..."

        n 2r "Oh, man."

        n "This is seriously a step backwards."

        mc "Eh?"

        n 2c "I liked your last two way better than this one."

        n 1k "I mean..."

        n "I guess I can't be mad at you for trying different things."

        n 1c "As long as you're not just trying to impress Yuri or something like that."

        n 5x "Gross."

        mc "Okay, okay."

        mc "Like you said, I'm allowed to try new things."

        label ch3_n_shared:

            show natsuki 5g

            mc "Why are you so emotionally invested in my poems, anyway?"

            mc "Isn't that more of a compliment to me?"

            n 1o "...Eh?"

            n 4x "N-No! Gross!"

            n 4w "It's not like I care!"

            n "It's just that {i}one{/i} of us in this club has to make sure you're not slacking off."

            mc "Really?"

            mc "Well, what if you ended up just scaring me away?"

            n 1t "That's--um..."

            n "...It's not like you would actually do that."

            mc "Yeah, you're right."

            mc "It's kind of fun to hang out here, even if I have to put up with you."

            show natsuki 1x

            mc "{i}Guh--!!{/i}"

            "Natsuki's elbow connects with my stomach."

            n 2y "Oh?"

            n "Maybe I won't mind scaring you away after all."

            mc "I was......just joking...."

            n 4z "Oh, I know!"

            n "Don't worry, I was too."

            n "Ahahaha!"

            show natsuki 4j

            mc "..."

            "How the hell do you call that a joke?"

            "That seriously hurt."

            "Well, maybe it was funny to her..."

            "...I guess that's kind of the point."

            "I should really just watch my mouth around Natsuki."

            n 2c "Anyway..."

            "Natsuki holds her poem out to me like nothing even happened."

            return

label ch3_n_med:

    if n_poemappeal[0] < 0 and n_poemappeal[1] < 0:
        jump ch3_n_bad12_shared
    elif n_poemappeal[1] != 0:
        n "..."

        n 2k "...This one's alright."

        mc "Alright?"

        n "Well, yeah."

        n "It doesn't blow me away."

        n "But there's nothing I really hate about it."

        n "It's just not really my style. I mean, that's fine."

        jump ch2_n_med_shared
    else:
        n "..."

        n 2k "...This one's alright."

        mc "Alright?"

        n "Well, yeah."

        n "About as good as yesterday's, anyway."

        n "I see what you're going for, but it's just not really my style."

        n 2a "I mean, that's fine."

        n "I'm mostly just glad that you're trying a little bit."

        mc "Well, of course I'm at least trying."

        jump ch3_n_shared

label ch3_n_good:

    if n_poemappeal[0] < 0 and n_poemappeal[1] < 0:
        jump ch3_n_bad12_shared
    elif n_poemappeal[0] > 0 and n_poemappeal[1] > 0:
        n 1l "Let's see, let's see!"

        mc "You're certainly enthusiastic today."

        n 2j "Of course."

        n "You know I like your writing."

        mc "I'm just surprised."

        mc "It seemed like you had a lot of trouble admitting that before."

        n 5w "Well... Well, of course!"

        n 5q "I just had to put you in your place a little bit!"

        n "It's not like..."

        n "I mean, it's not like I was shy or anything stupid like that."

        n 5t "Or jealous!"

        n "I really wasn't jealous."

        n "Just because you happen to be a good writer?"

        n 4y "That's such a dumb thing to get jealous about."

        n "Ahaha!"

        mc "Natsuki..."

        n 1h "What??"

        mc "You're not very confident about your writing, are you?"

        n 1n "...Eh?"

        n "W-What are you talking about?"

        n 1u "My writing is obviously the best..."

        n "...Right?"

        mc "..."

        "It took me a while to figure out, but I think I finally did."

        "Maybe Natsuki acts so arrogant because she's trying to make up for her own insecurities."

        "If she acts like she's the best, then other people might think that way, too."

        n 1m "Right...?"

        n "[player]..."

        n "Please just tell me you like my poems."

        n 1u "I don't care if you hate them."

        n "Just please tell me I'm the best."

        n "I just..."

        n 1q "I just really need to hear that from someone."

        n "I know I sound stupid."

        n "But there's a reason I never shared my poems before this."

        mc "Natsuki..."

        n "Because..."

        n 12c "Because nobody ever takes me seriously!"

        n "What's the point in sharing my poems if people just laugh and say \"That's so cute, just like you, Natsuki!\""

        n "Sometimes I don't want to be cute!"

        n 12d "But nobody understands that!"

        n "I try really hard when I write."

        n 12e "The style doesn't matter."

        n "The emotions are there."

        n 1n "Why can't anyone {i}see{/i} that...?"

        n 1u "I just want..."

        "Natsuki trails off."

        "Maybe it's because her lip started to quiver."

        "I look down."

        "Her fists are clenched really tightly."

        mc "Hey, Natsuki."

        mc "If you're not careful, you'll rip your own poem."

        "I gently grab the poem with my own hand until she relaxes her grip on it."

        "I place it flat on the desk and smooth out the wrinkles that she put into it."

        n 1h "D-Don't read it!"

        "Before I can pick it back up, Natsuki snatches the poem up from the desk."

        n 5q "It's not any good."

        n "And I know you hate my poems."

        n "So you don't have to read this one, okay?"

        mc "But I want to read it."

        n "W-Why?"

        mc "Because."

        mc "I like your poems."

        mc "I really do."

        show natsuki 5h

        mc "Why would I judge you for your style?"

        mc "It's not like my own style is anything crazy."

        mc "I mean, it's true that the first time I read one of your poems, I didn't look much into it."

        mc "But I know you better now."

        mc "And it's wrong for Yuri to think your style is more amateur than hers."

        mc "And Sayori... She always means well..."

        mc "But sometimes she's so focused on simple happiness that she doesn't understand what people really want."

        mc "Yeah... I guess I never really thought about how hard it is for you."

        mc "And I'm sorry if I was part of that problem."

        mc "I understand now."

        mc "You're not just cute, you're a lot more than that."

        show natsuki 12d

        mc "Ah-- Natsuki, you're doing it again--"

        "Once again, Natsuki clutches her poem a little too hard."

        "She looks down, hiding her eyes from me."

        "I never realized how difficult this was for her."

        "But finally, she forces herself to extend her arms and set her poem on the table."

        n 12e "You can...read it."

        n "Just turn that way."

        n "I don't want you to...look at my face right now."

        mc "Okay, I will."

        return
    elif n_poemappeal[0] > 0 or n_poemappeal[1] > 0:
        jump ch2_n_good_sharedwithch3
    else:
        n "..."

        n 2k "...Finally!"

        mc "Eh?"

        n 2l "This one. It's good!"

        n "I was wondering how long it would take you."

        mc "All right!"

        n 4y "Yeah, seriously."

        n "Don't listen to what anyone else says."

        n "Especially Yuri."

        n 4a "Just keep writing poems like this. That's all you need!"

        mc "Er..."

        mc "Are you sure that's not just what {i}you{/i} want?"

        n 2h "Excuse me?"

        n "You're talking to a pro, you know."

        n "Don't you think you should trust my opinion the most?"

        mc "I guess that depends."

        mc "Aren't you biased towards poems that are more simple and cute?"

        n 2w "Biased?"

        n "Of course not."

        n 4y "My opinion just happens to be the best."

        mc "..."

        "There's one thing I still can't tell."

        "Is Natsuki actually self-aware of her spoiled behavior?"

        "At this rate, I don't know if I'll ever figure it out."

        mc "...Fair enough."

        mc "I'm glad that you like my poem, after all."

        n 4z "Ahaha!"

        n 4j "I knew you'd finally understand."

        n "Just keep showing me your poems and you'll be a pro before you know it."

        n "Anyway, here's the one I wrote."

        return

label ch1_s_bad:

    s 1b "..."

    s "...Wow!"

    s "[player]..."

    s 4r "Your poem is really bad!"

    s "Ahahaha!"

    mc "Eh?!"

    s 4a "It's fine, it's fine~"

    s "It's your first time."

    s "Besides..."

    label ch1_s_shared:

        s 1a "I'm really happy just that you wrote one."

        s "It just reminds me of how you're really a part of the club now~"

        "(Not to mention the fact that I'm standing in front of you in the clubroom...?)"

        mc "Er...well, of course."

        mc "I'm not really into it yet, but that doesn't mean I'll break my promise."

        s 1d "See?"

        s "It's like I said before, [player]..."

        s "Deep down, you're not selfish at all, you know?"

        s "Trying new things like this for other people..."

        s 2q "That's something that only really good people do!"

        mc "Thanks...Sayori."

        "...I'm not sure if Sayori sees the full picture of my motive here."

        "Then again..."

        "I can't deny that she's part of the reason I joined."

        "Knowing how much this means to her and all..."

        s 1x "Yeah."

        s "And I'm gonna make sure you have lots of fun here, okay?"

        s "That will be my way of thanking you~"

        mc "Alright, I'm going to hold you to that, then."

        s 4r "Yay~!"

        s "Now, you'll read my poem too, right?"

        s 1y "Don't worry, I'm really bad at this."

        s "Ehehe..."

        mc "We'll see about that."

        return

label ch1_s_med:

    s "..."

    s 2x "This is a good poem, [player]!"

    s "Are you sure it's your first time?"

    mc "Of course..."

    mc "It's not that good."

    mc "Am I the kind of guy who would be writing poems in his spare time?"

    s 2q "Ehehe, I guess you're right~"

    s 1q "But that's why it impressed me!"

    s 1d "Well, to be honest..."

    s "I was afraid that you wouldn't do it seriously..."

    s "Or that you wouldn't write one at all."

    jump ch1_s_shared

label ch1_s_good:

    s 1n "..."

    s "...Oh my goodness!"

    s 4b "This is sooooo good, [player]!"

    mc "Eh?"

    s 4r "I love it~!"

    s "I had no idea you were such a good writer!"

    mc "Sayori..."

    mc "You must be seriously overreacting."

    mc "I'm not a good writer at all."

    mc "I honestly have no idea what I'm doing."

    s 1x "Well..."

    s "Maybe that's why!"

    s "Because I have no idea what I like, either!"
    s 1r "Ahahaha!"

    mc "Jeez..."

    if y_readpoem:
        "Yuri's opinion was way more constructive than this..."
    else:
        "I'm sure Yuri's opinion has to be a little more constructive than this."

    if not n_readpoem:
        "Maybe even Natsuki's."

    mc "Are you sure you don't like it just because I wrote it?"

    s 1b "Eh?"


    s "Well, I'm sure that's part of it."

    s 1x "I think I understand you better than a lot of other people, you know?"

    s "So when I read your poem..."

    s "It's not just a poem..."

    s 4q "It's a [player] poem!"

    s "And that makes it feel extra special!"

    s "Like I can feel your feelings in it~"

    "Sayori hugs the sheet against her chest."

    mc "You're so weird, Sayori..."

    s "Ehehe..."

    jump ch1_s_shared

label ch2_s_bad:

    s "..."

    s 1q "Ehehe, I love reading your poems~"

    s "It's like I never know what I'm going to get!"

    mc "So basically you're saying it sucks."

    s 4c "No! Not at all!"

    s 4l "...Maybe!"

    s 5a "Just a little?"

    s "Yuri must have spoiled me a little bit with her poems..."

    s "Ehehe..."

    mc "It's fine, it's fine."

    mc "After all, I still have no idea what kinds of writing you even like."

    label ch2_s_shared:

        s 1q "Yeah!"

        s "Me neither!"

        mc "Ugh..."

        mc "Why don't you at least try giving it some thought?"

        s 2d "Aww, you want to write something for me?"

        s "That's so sweet~"

        mc "Yeah, right."

        mc "But you're always thinking about other people."

        mc "You need to think about yourself once in a while."

        mc "If you don't, you might end up getting hurt at some point."

        s 1n "Ehh?"

        s "Well..."

        s 1o "I don't really know what you mean, but I'll try to keep it in mind!"

        mc "Well, whatever..."

        s 1b "Anyway, let's see..."

        s "Hmm..."

        s 4q "I guess I like...happy poems~"

        s 4i "Wait, sometimes I like sad poems too..."

        s 1i "Sometimes a little bit of both..."

        s "There's a word for that, right...?"

        s "What's the word I'm looking for..."

        s 4r "...Bittersweet!"

        s "Yeah!"

        s 1x "I like things that are happy and things that are sad."

        mc "Happy and sad?"

        mc "I can't see you liking something sad, Sayori..."

        s 1c "Well..."

        s "I like happy the most!"

        s 1d "But sometimes when you have a little raincloud in your head..."

        s "A sad poem can help give the raincloud a little hug..."

        s 4q "...And make a nice happy rainbow!"

        mc "...Sayori, that's unexpectedly poetic."

        s 4n "Eh? It is?"

        s "Maybe I'm getting better at expressing my feelings after all!"

        s 2q "Thanks, [player]!"

        s "I should go write that down, then~"

        s 2a "You can read my poem now, okay?"

        return

label ch2_s_med:

    if s_poemappeal[0] < 0:
        s "..."

        s 4x "Ooh!"

        s "I like this one, [player]!"

        s "It has some nice feelings in it~"

        mc "Ah, I'm glad."

        mc "So it's at least better than yesterday's."

        s 1q "Uh-huh!"

        mc "Maybe I'm getting better at this, then."

        label ch2_s_med_shared:

            s 1a "Well, I'm not very good at figuring out if poems are good or bad..."

            s "But that's why I just go by my heart~"

            s "If it makes me feel things, then it must be a good poem!"

            "I'm not sure that's exactly how it works..."

            "...Then again, I guess conveying feelings is a pretty important part of this whole thing."

            mc "Yeah, maybe..."

            mc "Honestly, I don't even know what kind of writing you like in the first place."

            jump ch2_s_shared
    elif s_poemappeal[0] == 0:
        s "..."

        s 4x "Ooh!"

        s "I like this one, [player]!"

        s "It has some nice feelings in it~"

        mc "Ah, I'm glad."

        mc "Does that mean it's better than yesterday's?"

        s 4b "Mmm, lemme think..."

        s 1q "I dunno!"

        s "I guess I like them both!"

        s "Ehehe~"

        mc "That's not very helpful, you know..."

        jump ch2_s_med_shared
    else:
        s "..."

        s 4x "Ooh!"

        s "I like this one, [player]!"

        s "It has some nice feelings in it~"

        mc "Ah, I'm glad."

        mc "Still, though..."

        mc "Your tone makes it sound like you liked yesterday's poem better."

        s 2l "Ehehe, I guess you caught me..."

        s "Sometimes you know me a little too well for my own good!"

        mc "Well, don't just try to be nice about it."

        mc "If I'm doing a bad job then I'd rather just hear it."

        s 1c "No, no!"

        s "I still liked this one! I promise!"

        s 1h "You know I wouldn't lie to you, [player]...!"

        s "Never ever!"

        mc "Yeah, I guess so..."

        mc "What made yesterday's poem so great compared to this one, then?"

        s 1b "Umm....."

        jump ch2_s_med_shared

label ch2_s_good:

    if s_poemappeal[0] < 1:
        s 1n "..."

        s "...Oh my goodness!"

        s 4r "This is sooooo good, [player]!"

        mc "Eh?"

        s "I love it~!"

        s "Especially after yesterday's poem!"

        mc "Ugh..."

        mc "You're too honest sometimes, Sayori."

        s 4x "No, but really!!"

        s 1x "I wanna put this on my wall~"

        s "Can I?"

        mc "Sayori..."

        mc "You must be seriously overreacting."

        mc "I'm not a good writer at all."

        mc "I honestly have no idea what I'm doing."

        s 1l "Well..."

        s "Maybe that's why!"

        s "Because I have no idea what I like, either!"

        s 4r "Ahahaha!"

        mc "Jeez..."

        "I'm sure Yuri's opinion has to be a little more constructive than this."

        "Maybe even Natsuki's."

        mc "Are you sure you don't like it just because I wrote it?"

        s 4b "Eh?"

        s 1b "Well, I'm sure that's part of it."

        s "I think I understand you better than a lot of other people, you know?"

        s "So when I read your poem..."

        s "It's not just a poem..."

        s 4q "It's a [player] poem!"

        s "And that makes it feel extra special!"

        s "Like I can feel your feelings in it~"

        "Sayori hugs the sheet against her chest."

        mc "You're so weird, Sayori..."

        s 4l "Ehehe..."

        jump ch2_s_med_shared
    else:
        s "..."

        s 1d "[player]..."

        s "I really love your poems."

        s "I can't believe you've been hiding these from me!"

        mc "Eh? I'm not hiding anything!"

        s 1b "But..."

        s "Your poems are sooo good..."

        s "Yesterday's, and this one too!"


        s "You can't tell me you haven't done this before!"

        mc "I mean..."

        mc "You're really the only one who feels that way, so..."

        s 4h "Eh?!"

        s "No way!!"

        s "Not even Natsuki...?"

        mc "Well, I guess Natsuki is the least likely to admit how much she likes something..."

        mc "But I don't think it's that."

        s 1b "What do you mean?"

        mc "Well..."

        mc "I guess I'll be honest about it."

        mc "It's a lot easier to write poems when I'm thinking about you."

        s 4m "E-Eh?!"

        s "Wawawa--!"

        mc "Stop thinking weird things, idiot!"

        mc "I just mean that you're a really...expressive person, I guess."

        mc "How am I supposed to write poems about my own stupid life?"

        mc "But you somehow make everything in your life an adventure."

        mc "Even the little things."

        s 4o "Like cooking!!"

        mc "Let's not talk about that!"

        s 5a "Ehehe..."

        mc "So, yeah..."

        mc "I guess what I'm saying is that I can feel more feelings through you than I can through myself."

        mc "We have that kind of weird connection."

        mc "It's your fault for getting in my business all the time."

        s 1e "Ehh...?"

        s "I don't know if I understand..."

        mc "Sigh..."

        mc "You never understand when I try to explain things to you, do you, Sayori?"

        "I pat Sayori's head."

        s 4s "Ahaha! Heyyy!"

        s "I'm not a kid, you know!"

        mc "Are you sure about that?"

        s 4l "Mmmm, maybe~"

        "Sayori starts fiddling with her pencil between her hands."

        s "Hey, [player]..."

        s 2d "Will you give me your poem?"

        s "I kinda want to keep it."

        mc "Huh? Why?"

        s 1y "Because..."

        s "Well..."

        s "It's the first time you've written something for me..."

        s "Ehehe..."

        mc "!!"

        mc "Sayori, you completely misunderstood!"

        mc "I didn't write this for you!"

        s 5b "Ehehehehe..."

        mc "Sigh..."

        mc "Are you even listening anymore?"

        mc "Well, whatever."

        mc "I'll give it to you when we go home."

        show sayori at h11

        s 4m "Really?!"

        "{i}Snap!{/i}"

        s 4p "A-Ah!!"

        s "I broke my pencil..."

        "Sayori hastily bends down to pick up the piece she dropped."

        "But being inattentive of her surroundings, she bumps right into me."

        s 4l "S-S-Sorry--!!"

        mc "It's fine, it's fine."

        mc "I'll get it for you."

        "I bend down and pick up the broken pencil."

        "Sayori clutches the desk beside her to support herself, knees shaking."

        s 5b "I-I'm a little clumsy today..."

        s "Ahahaha..."

        mc "Let's sit down, Sayori..."

        s 4y "Y-Yeah..."

        "I grab Sayori's arm and help her sit at the desk."

        mc "Anyway, I still haven't read your poem..."

        s 4b "Oh!"

        s "Sorry, I forgot about that~"

        s 1h "But it's not as good as yours!!"

        mc "Jeez, don't worry."

        mc "I'm sure I'll like it."

        return

label ch3_s_bad:

    $ currentname = "Yuri"

    if n_poemappeal[2] > y_poemappeal[2]:
        $ currentname = "Natsuki"

    s "..."

    s 1k "...Hm."

    s "It's nice, I guess~"

    mc "Come on, I can already tell you don't like it."

    s 1d "Well..."

    s "You don't need to worry about what I think."

    s 2y "After all, you wrote this for someone else, didn't you?"

    s "Probably [currentname]..."

    mc "Eh??"

    mc "I didn't write this for anyone specifically!"

    s "Maybe..."

    s 1d "That's not really what I meant, though."

    s "But it's okay."

    s "You're making new friends, just like I was hoping."

    s 1q "That makes me...really happy."

    s "And you're happy too, right?"

    s 1a "In this club?"

    mc "Well..."

    mc "Of course I am."

    s 4q "Good~"

    s "That's all that matters to me."

    s 1d "Thank you, [player]."

    mc "Sayori..."

    mc "Is there something wrong?"

    s 1b "Huh?"

    s 1k "No, nothing."

    s "I'm just a little tired today."

    s 1l "Ehehe."

    mc "Alright..."

    mc "Just tell me if you need anything."

    s 1a "I will."

    s "Don't worry about me, okay?"

    s "You can go play with everyone else now."

    mc "If you insist..."

    s 4q "Yaay~"

    s 4a "I'm gonna go home a little bit early today."

    mc "Sayori...?"

    s 1q "Tell Monika I wasn't feeling well, okay?"

    s "I'll see you tomorrow~"

    "Before I can say anything else, Sayori cheerfully walks out of the classroom, humming to herself."

    $ skip_poem = True

    return

label ch3_s_med:

    jump ch3_s_bad

label ch3_s_good:

    if poemwinner[0] != "sayori" and poemwinner[1] != "sayori":
        jump ch3_s_bad

    s 1d "..."

    s "This is your best one so far."

    s "It's really really nice, [player]~"

    mc "Er-- Thanks."

    s 1q "Mhm~"

    mc "..."

    mc "Sayori, you've been a little quiet today."

    mc "Is everything alright?"

    s 4m "E-Eh??"

    s "Of course!"

    s 4l "Everything is fine~"

    s "Maybe I'm just a little tired today."

    s 1l "Ehehe."

    mc "Do you want to nap or something?"

    s 1h "No, that's silly!"

    s "Don't worry about me, okay?"

    s 1q "I only want to see smiles on your face~"

    mc "Well, alright..."

    s 1b "Hey, [player]..."

    s "I'm still a little surprised."

    s "I really thought that you would try writing your poems like the way Yuri does..."

    s 1y "Or even Natsuki..."

    s "But in the end..."

    mc "...Yeah."

    mc "I guess you're the one who likes this one the most."

    stop music fadeout 1.0

    s 1k "...Why?"

    s "You don't want to get closer with everyone else?"

    play music t9

    mc "Wait!"

    mc "Of course I do!"

    mc "But that doesn't mean I need to try so hard to impress them."

    mc "I still understand you the most, Sayori."

    mc "I know you have to sometimes put up with me."

    mc "And I have to sometimes put up with you."

    mc "But we have...a wavelength or something."

    mc "And this is how the poem came out."

    mc "Sometimes it feels like you're the only exciting thing in my life."

    mc "So sometimes it's just easier to write when thinking about you."

    mc "...Sayori?"

    s 4v "N-No..."

    s "[player]..."

    s "I don't...deserve this..."

    s "You're too nice to me..."

    s "Why are you doing this...?"

    "Sayori has trouble keeping her voice steady, all of a sudden."

    s "If you had fun with everyone else instead..."

    s "This would be...so much easier!"

    mc "Sayori...!"

    "I glance around the room to make sure nobody has noticed this."

    mc "Sayori."

    mc "I've probably never said this before, but I don't understand what you're feeling right now."

    mc "Tell me what will cheer you up."

    "Sayori shakes her head."

    "She sniffles and keeps shaking her head."

    "Finally, she gathers herself and puts on a smile."

    s 1y "It's nothing, [player]."

    s "It's just a little raincloud."

    s 4r "I'm sorry you had to see that. Ahahaha!"

    s "I promise it won't happen again."


    s 1a "Just smiles from everyone, okay?"

    s "That's all that matters."

    s "Go play with everyone else."

    s "I'm gonna go home a little bit early today~"

    mc "Sayori--"

    s 2q "Tell Monika I wasn't feeling well, okay?"

    s "I'll see you tomorrow~"

    "Before I can say anything else, Sayori cheerfully walks out of the classroom, humming to herself."

    $ skip_poem = True

    return

label ch1_y_bad:

    y 1g "..."

    y "Mm..."

    y "..."

    "Yuri stares at the poem."

    "A minute passes, more than enough time for her to finish reading."

    mc "Um..."

    y "Oh!"

    y 3n "S-Sorry...!"

    y "I forgot to start speaking..."

    y "U-Um!"

    mc "It's fine, don't force yourself."

    y 2v "I'm not..."

    y "I just need to put my thoughts into words."

    y "Hold on..."

    y "...Okay."

    y 1f "This is your first time writing a poem, right?"

    mc "Er, yeah..."

    mc "Why do you ask?"

    y "I'm just making sure."

    y "I guessed that it might be after reading through it."

    mc "Ah, so it's that bad."

    y 2p "No!!"

    y 2o "...Did I just raise my voice...?"

    y 4c "Uu, I'm so sorry..."

    "Yuri buries her face in her hands."

    "I couldn't help but notice that it's been several minutes and we really haven't gotten anywhere."

    "It might take Yuri a while to get used to new people..."

    mc "It's fine, I really didn't notice."

    mc "What were you saying?"

    y 2u "Right...um..."

    label ch1_y_shared:

        y 1a "It's just that there are specific writing habits that are usually typical of new writers."

        y "And having been through that myself, I kind of learned to pick up on them."

        y 1i "I think the most noticeable thing I recognize in new writers is that they try to make their style very deliberate."

        y "In other words, they tend to pick a writing style separate from the topic matter, and they form-fit the two together."

        y 1a "The end result is that both the style and the expressiveness are weakened."

        "Once Yuri finds her train of thought, it's as if her demeanor totally changes."

        "Her stammering is completely gone, and she sounds like an expert."

        y 1k "Of course, that's not something you can be blamed for."

        y "There are so many different skills and techniques that go into writing even a simple poem."

        y 1a "Not just finding them and building them, but getting them to work together is probably the most challenging part."

        y "It might take you some time, but it all comes with practice, and learning by example, and trying new things."

        y "I also hope that everyone else in the club gives you valuable feedback."

        y 1l "Natsuki can be a little bit biased, though..."

        mc "Biased? How?"

        y 2j "U-Um..."

        y "Well..."

        y "Never mind..."

        y "I shouldn't be talking about people like that..."

        y "Sorry..."

        mc "It's fine."

        "I'm not sure if Yuri is apologizing to herself, to me, or to Natsuki."

        mc "Do you mind if I read your poem now?"

        y 3c "Please do!"

        y "I'd love to share my thought process behind it..."

        "Yuri smiles dreamily, as if that's a rare opportunity for her."

        "Which itself is kind of funny..."

        "...After all, isn't this supposed to be a literature club?"

        return

label ch1_y_med:

    jump ch1_y_bad

label ch1_y_good:

    y 1e "..."

    "As Yuri reads the poem, I notice her eyes lighten."

    y 2f "...Exceptional."

    mc "Eh? What was that?"

    y "...?"

    y 2n "D-Did I say that out loud...?"

    "Yuri first covers her mouth, but then ends up covering her whole face."

    y 4c "I...!"

    y "Uu..."

    y "{i}(He's going to hate me...){/i}"

    mc "Um..."

    mc "You really didn't do anything wrong, Yuri..."

    y 4a "Eh...?"

    y "That's..."

    y 2q "I-I guess you're right..."

    y "What am I getting so nervous for?"

    y "A-Ahaha..."

    show yuri 2l at t11

    "Yuri takes a breath."

    y "So..."

    y 1a "What kind of writing experience do you have?"

    y "Your use of imagery and metaphors indicates you've written a lot of poetry before."

    mc "Really...?"

    mc "Wow, that's a huge compliment coming from you."

    mc "This is actually my first time, really."

    y 1e "Huh...?"

    "Yuri stares at me blankly, then looks at my poem again."

    y "..."

    y 2h "...Well, I know that!"

    y "I just meant...u-um..."

    "Yuri trails off, unable to find an excuse."

    "She traces her finger along the words in the poem, as if breaking it down more thoroughly."

    y 2l "...Yeah."

    y "Okay."

    y "This is the reason I was able to tell."

    jump ch1_y_shared

label ch2_y_bad:

    if y_poemappeal[0] < 0:
        y "..."

        y 2h "Um..."

        y "...Are you still mad at me?"

        mc "Eh?!"

        y "For disrespecting Natsuki yesterday..."

        y "Because reading this poem..."

        y "Now I know why you got mad at me."

        y "Because you..."

        y 3v "You prefer her writing over mine!"

        mc "That's not really true...!"

        y "Meaning when I disrespected her..."

        y "I disrespected you too...didn't I?"

        y 4c "Oh no..."

        mc "Yuri..."

        mc "You might be reading into this a little too much..."

        y "How could I be so stupid...?"

        y "I always let these things happen..."

        y "Whenever I think before I speak, I just come off as awkward and unlikable."

        y "But if I speak without thinking, the things I want to keep inside come out and make people hate me."

        y 2v "So...please don't force yourself to be around me."

        y "I know this is what Monika wants."

        y "But it's not fair to you when you could be enjoying your time with Natsuki and Sayori."

        mc "Yuri--"

        y 4b "Please..."

        y "It makes it easier for me if you don't express any concern."

        y "Besides..."

        y "I have my books with me."

        y 3u "That's...all I need."

        mc "..."

        "Yuri smiles sadly and puts her head down on her desk."

        "I'm frustrated."

        "I don't hate her, but it's as if she's not capable of listening to me over her own thoughts."

        "I sigh to myself."

        "All I can do is accept that that's how she is."

        "If she wants to be left alone, then I have no choice but to abide to that request."

        $ skip_poem = True

        return
    else:
        y 2a "Ah, is it my turn?"

        y "Let's see how it compares to yesterday's..."

        y "Mm..."

        y "I see..."

        y "It's a bit different."

        y 1a "I respect you for trying different things, [player]."

        y "Were you inspired by Natsuki's poem?"

        y "Or Sayori's, perhaps?"

        mc "Well..."

        mc "I guess you could say that..."

        y "I thought so."

        y 2u "I'm happy for you."

        y "You don't need to find inspiration in my poems."

        y "I write them for myself..."

        y 4b "...Not for anyone else."

        y "So I don't really...need for people to like them or anything."

        mc "Yuri!"

        y 3t "E-Eh?"

        mc "I'm sorry for being blunt, but you're overthinking this a little."

        mc "Just because our styles are different doesn't mean I dislike your poems..."

        mc "In fact, if I tried to do something in your style, I would probably just do a terrible job."

        y 4a "I...I see..."

        y "I'm sorry..."

        y "My stupid mind...it likes to do that sometimes."

        y "Anyway..."

        label ch2_y_shared:

            y 2h "You don't need to be afraid to be a little more daring..."

            y "Metaphors can go a long way."

            y "Don't feel like you need to work your brain like turning a bunch of gears."

            y 1m "Try letting your mind wander through your feelings..."

            y "And write down the things you see and hear."

            y "That's one way to truly enable your reader to see into your mind."

            y 2u "It's a very intimate exercise..."

            mc "I see."

            mc "That's a certainly interesting technique."

            mc "Thanks for sharing."

            y 2v "I have, um..."

            y "...Well, an example of that, if you'd like to read it..."

            mc "Of course."

            mc "Is this the poem you wrote for today?"

            "Yuri nods, and timidly hands me her poem."

            return

label ch2_y_med:

    if y_poemappeal[0] <= 0:
        y 1a "Let's see what you've written for today."

        y "..."

        y "Mm..."

        y 1c "Well done, [player]."

        y "Your skills are already improving."

        mc "Really?"

        mc "Thanks, Yuri."

        mc "Coming from you, that means a lot."

        y 3f "Eh?"

        y 3v "I-It's nothing!"

        y "I'm just happy to help inspire fellow writers..."

        y "I know you're new to this, so don't worry so much if it seems like you can't get your poem to feel perfect."

        jump ch2_y_shared
    else:
        y 1a "Let's see what you've written for today."

        y "..."

        y "Mm..."

        y "This is pretty good, [player]."

        y "Were you influenced by seeing everyone's writing styles yesterday?"

        mc "I guess you could say that..."

        y 1m "I was also a bit surprised by how differently everyone writes."

        y "So I respect you for trying new things."

        jump ch2_y_shared

label ch2_y_good:

    if y_poemappeal[0] < 1:
        y 1a "Let's see what you've written for today."

        y "..."

        y 2e "......"

        "Yuri stares at the poem with a surprised expression on her face."

        mc "Do you...like it?"

        y "[player]..."

        y "...How did you pick up on this so quickly?"

        label ch2_y_good_shared:

            y 2v "Just yesterday, I was telling you the kind of techniques worth practicing..."

            mc "Maybe that's why..."

            mc "You did a good job explaining."

            mc "I really wanted to try giving it more imagery."

            show yuri 4b zorder 2 at t11
            "Yuri visibly swallows."

            "Even her hands appear sweaty."

            y "I'm not...used to this..."

            mc "Used to what?"

            y 3o "I don't know...!"

            mc "It's fine, take your time..."

            show yuri 3l at t11

            "Yuri breathes and collects her thoughts."

            "I know that Yuri likes to think before she speaks, so I offer that patience to her."

            y 4a "Yeah..."

            y "Just...being appreciated like this...I guess."

            y "It probably sounds really stupid..."

            y "But seeing someone motivated by my writing..."

            y "It just makes me..."

            y "Really happy..."

            mc "Are you saying you've never shared your writing before?"

            "Yuri nods."

            mc "Really? I don't believe it."

            y "I really only write for myself..."

            y "And besides..."

            y 3w "...People would just laugh at me!"

            mc "Do you really think that...?"

            "Again, Yuri nods."

            mc "Huh..."

            mc "Even your close friends?"

            y 2v "..."

            "Yuri doesn't respond to that."

            "I wonder why..."

            mc "Anyway..."

            mc "Do you want to share the poem you wrote today?"

            y "...Yeah."

            y 3t "I do!"

            y "If it's with you..."

            return
    else:
        y 1a "Let's see what you've written for today."

        y "..."

        y 2e "......"

        "Yuri stares at the poem with a surprised expression on her face."

        mc "Do you...like it?"

        y "[player]..."

        y "This one might even be better than yesterday's..."

        y "...How did you even pick up on this so quickly?"

        jump ch2_y_good_shared

label ch3_y_bad:

    if y_poemappeal[0] < 0 and y_poemappeal[1] < 0:
        label ch3_y_bad12_shared:

            y 4b "..."

            "Yuri doesn't look too enthusiastic about spending time with me..."

            "I guess if she changes her mind, she'll come to me."

            "But I should leave her be for now."

            $ skip_poem = True

            return
    elif y_poemappeal[1] < 0 or y_poemappeal[0] < 0:
        y 1i "..."

        y "...I see."

        y "I think you're improving at writing in general, [player]."

        y 2i "But I can't help but feel a little bit foolish."

        mc "Eh? What for?"

        y "Just..."

        y "I feel like I kept trying to offer advice..."

        y "When it should have been clear to me that you prefer a different writing style."

        y 3w "I probably just sounded arrogant!"

        y "I'm so stupid..."

        mc "Yuri, that's a little--"

        y 4b "No..."

        y "You don't understand."

        y "I spent so much time worrying about what's better and what's worse."

        y "Not just with you..."

        y "With Natsuki, and Sayori..."

        y "It's obvious now why nobody has fun when talking to me..."

        y "And because of that..."

        y 4c "...I'll just keep my mouth shut about your poem!"

        mc "..."

        "Yuri buries her head into her arms on her desk."

        "That's not the first time I've seen her do that."

        mc "I don't think it's ever as bad as you make it sound in your head..."

        y "..."

        mc "I think if people really didn't like talking to you..."

        mc "Then it would be a lot more obvious."

        mc "I know that you like to read deeply into things."

        mc "But some things are just worth taking at face value."

        y 4b "I just..."

        y "I've gotten so used to it..."

        y "...That it's hard for me to comprehend any other possibility."

        mc "Gotten used to what?"

        mc "Reading deeply into things?"

        y "Being disliked."

        mc "Yuri..."

        y 2v "What...what am I saying?"

        y "I'm sorry..."

        y "I never meant to bring this up..."

        "Yuri turns away from me."

        y 4b "You should go..."

        mc "Eh...?"

        y "Please..."

        y "Please don't look at me right now."

        y "I want to do some thinking..."

        mc "Are you sure...?"

        "Yuri nods."

        mc "Alright..."

        "I leave Yuri be."

        "Comforting or reassuring her is nearly impossible as it is."

        "So when she wants to be alone, I think anything I say could only make things worse."

        "I feel bad, but thankfully she doesn't take it out on me..."

        "I'll wait until she's feeling a little bit better."

        $ skip_poem = True

        return
    else:
        y 1a "..."

        y "...Ah."

        y "Decided to try something different today?"

        mc "I guess so."

        mc "Is that good, or bad?"

        y 2g "Well, neither."

        y "I have my preferences."

        y "But it would be unfair of me to call something good or bad based on that."

        label ch3_y_shared:

            y 1f "As always, I believe what's most important is exploring and discovering yourself."

            mc "That's comforting."

            mc "I'm kind of afraid of disappointing you in some way or another."

            y 2t "Eh...?"

            y "Why me...?"

            mc "Well, you're always sophisticated with your writing and have the most advice to share."

            y 4a "Is that so...?"

            y "..."

            "Yuri thinks for a good minute."

            y 4c "...That must be terrible."

            mc "Eh?"

            y "For me to have become someone whose opinion is fearsome..."

            y "How unlikable of me..."

            mc "Yuri..."

            mc "It's not as bad as you're making it sound in your head."

            mc "I just meant that I respect your opinion."

            y 2v "I see..."

            y "I'm sorry that I always overthink and come to those sorts of conclusions..."

            y "I'm just...a little too used to it."

            mc "Overthinking?"

            y "Being disliked."

            mc "Yuri..."

            y 3w "What...what am I saying?"

            y "I'm sorry, I didn't mean to bring that up..."

            y "Let's move on..."

            mc "Alright..."

            mc "Do you want to share your poem now?"

            y 2i "Okay..."

            y "Here."

            return

label ch3_y_med:
    if y_poemappeal[0] < 0 and y_poemappeal[1] < 0:
        jump ch3_y_bad12_shared
    elif y_poemappeal[0] < 1 or y_poemappeal[1] < 1:
        y "..."

        y 1a "Well done, [player]."

        y "You've definitely improved your writing over the course of these few
        days."

        y "Has my advice been helpful to you?"

        mc "Yeah... Definitely."

        y 2m "I'm glad..."

        y "Sharing our writing like this..."

        y 2a "It's a lot more fun and rewarding than I anticipated."

        y "I need to remember to thank Monika..."

        y "I think we all felt a little awkward at first."

        y 1a "But now it seems like everyone is enjoying sharing their writing and seeing what others think."

        mc "I guess I can't really disagree."

        mc "I was afraid this whole thing would be a chore..."

        "But it's a great way for me to spend some personal time with all the girls in the club."

        mc "But it's been fun getting to know everyone and their writing."

        mc "And I guess doing some writing myself..."

        y 2a "Well..."

        y "Have you learned anything about yourself, [player]?"

        mc "Eh?"

        y 2i "Well, you know how I like to say that writing is a very personal way to get in touch with yourself..."

        y 1a "In the end, it doesn't matter if you're a good writer, or a bad writer."

        y "And even my opinions are just opinions...you know?"

        jump ch3_y_shared
    else:
        y 1e "..."

        y "...Ah."

        y "Decided to try something different today?"

        mc "I guess so."

        mc "Is that good, or bad?"

        y 2i "Well, neither."

        y "I have my preferences."

        y "But it would be unfair of me to call something good or bad based on that."

        jump ch3_y_shared

label ch3_y_good:

    if y_poemappeal[0] < 0 and y_poemappeal[1] < 0:
        jump ch3_y_bad12_shared

    if y_poemappeal[1] < 1:
        y "..."

        y 2u "[player]..."

        y "...This is wonderful."

        y "I can feel the emotion that you poured into it."

        y "Is this the result of trying what I suggested yesterday?"

        mc "Yeah, I guess so..."

        mc "You did a good job explaining."

        mc "I really wanted to try giving it more feeling."

        show yuri 4b zorder 2 at t11
        "Yuri visibly swallows."

        "Even her hands appear sweaty."

        play music t9 fadeout 1.0

        y "I'm not...used to this..."

        mc "Used to what?"

        y 3o "I don't know...!"

        mc "It's fine, take your time..."

        "Yuri breathes and collects her thoughts."

        "I know that Yuri likes to think before she speaks, so I offer that patience to her."

        y 4a "Yeah..."

        y "Just...being appreciated like this...I guess."

        y "It probably sounds really stupid..."

        y "But seeing someone motivated by my writing..."

        y "It just makes me..."

        y "Really happy..."

        mc "Are you saying you've never shared your writing before?"

        "Yuri nods."

        mc "Really? I don't believe it."

        y "I really only write for myself..."

        y "And besides..."

        y 3w "...People would just laugh at me!"

        mc "Do you really think that...?"

        "Again, Yuri nods."

        mc "Huh..."

        mc "Even your close friends?"

        y 2v "..."

        "For some reason, Yuri doesn't respond."

        mc "Yuri...?"

        label ch3_y_good_shared:

            if not renpy.music.get_playing(channel='music') == audio.t9:
                play music t9 fadeout 1.0

            "Yuri smiles sadly."

            y 1u "[player], during lunchtime, I eat by myself."

            y "Did you know that?"

            y "It's a great time to find a quiet spot and do some reading."

            y "In fact..."

            y 2s "I always have some books with me."

            y "You could say I really enjoy reading..."

            y "...Well, that's one way to put it, anyway..."

            y "But..."

            y "Books are so full of amazing and inspiring people."

            y "People you want to fall in love with."

            y "Or people you just know would make a really good friend."

            y 1m "Cheerful people, who always put a smile on your face..."

            y "Or deep thinkers, and problem solvers, who discover the mysteries of life."

            y "So when you look at it that way..."

            y "I'm surrounded by friends every day..."

            y "...You know?"

            y 2s "And those friends don't laugh at me..."

            y "They don't tease me for spacing out all the time..."

            y "They don't make fun of my body type..."

            y "And..."

            y 3v "...And they don't hate me for acting like a know-it-all!"

            mc "People...say that about you?"

            y "I'm not a know-it-all, [player]!"

            y "It's the opposite. I don't know anything!"

            y 4b "I don't know how to talk to people."

            y "I don't know how to make people see me as normal."

            y "I don't even know how to make myself happy!"

            y "I have all these feelings..."

            y "And all I can do with them is read, and write..."

            y "But it wasn't until now..."

            y 2s "That I started sharing it with you..."

            y "...That I really understood what was missing all this time."

            mc "But I haven't really done anything..."

            y "No..."

            y "That's wrong."

            y "Just being patient and respectful..."

            y 3u "That's really...important to me."

            y "I know I'm a difficult person, [player]..."

            y "I speak too slowly..."

            y "I second-guess myself all the time..."

            y "I read too deeply into things..."

            y "But every time..."

            y "You've always treated me just like anyone else."

            y "It's so rare that I feel comfortable with myself when I talk to others..."

            y "But that's why every time I talk to you..."

            y 2s "...I just feel really happy."

            mc "I see..."

            mc "Well, I treat you how you deserve to be treated, Yuri."

            mc "And if other people don't see it that way, then screw them."

            mc "I mean, I joined this club hoping I would make friends."

            mc "And I would say I've had at least one success."

            mc "Wouldn't you?"

            y 4b "U-Um..."

            y "If you put it that way..."

            y "...Yeah..."

            y 4e "We really are friends now, aren't we?"

            "Yuri puts her head in her hands."

            "But this time, she's smiling as she does it."

            mc "Do you want to show me your poem?"

            y 3s "Yeah."

            y "I do!"

            y "Let me get it for you..."
        return
    else:
        y "..."

        y "[player]."

        y 2s "Your writing has only improved in these last few days."

        y "Every poem you've shown me has been nothing short of spectacular."

        y "I can really feel the emotions..."

        y 2m "I'm a little envious, even..."

        y "I don't think it ever came to me this naturally."

        mc "Yuri, that's the wrong way to put it."

        mc "This never did come naturally to me."

        mc "But I've been able to improve so much thanks to you."

        mc "You're really the example I was chasing after."

        y 3u "I-Is that so...?"

        "Yuri gently smiles to herself."

        y "This feeling..."

        y "I'm so glad...I got the chance to share my writing."

        y 4e "I never thought it would feel like this."

        mc "I remember you mentioning that yesterday."

        mc "I can't believe that you're so good at something and you've never even shared it with anyone."

        mc "It's kind of a shame."

        y 2u "Maybe, but..."

        y "It's not like I really...had a choice."

        mc "What do you mean...?"

        y "Well..."

        jump ch3_y_good_shared

label ch1_m_start:

    m 1b "Hi, [player]!"

    m "Having a good time so far?"

    mc "Ah...yeah."

    m 1k "Good! Glad to hear it!"

    m 4a "By the way, since you're new and everything..."

    m "If you ever have any suggestions for the club, like new activities, or things we can do better..."

    m 4b "I'm always listening!"

    m "Don't be afraid to bring things up, okay?"

    show monika 4a

    mc "Alright...I'll keep that in mind."

    "Of course I'll be afraid to bring things up."

    "I'm much better off just going with the flow until I'm more settled in."

    m 1a "Anyway..."

    m "Want to share your poem with me?"

    mc "It's kind of embarrassing, but I guess I have to."

    m 5a "Ahahaha!"

    m "Don't worry, [player]!"

    m "We're all a little embarrassed today, you know?"

    m "But it's that sort of barrier that we'll all learn to get past soon."

    mc "Yeah, that's true."

    "I hand Monika my poem."

    m 2a "...Mhm!"

    $ nextscene = "m_" + poemwinner[0] + "_" + str(eval(poemwinner[0][0] + "_appeal"))

    call expression nextscene

    mc "I'm sure I'll end up trying different things a lot."

    mc "It could take a while before I feel comfortable doing this."

    m 1k "That's okay!"

    m 1b "I'd love to see you try new things."

    m "That's the best way to find the kind of style that suits you."

    m 3e "Everyone else might be a little bit biased toward their own kinds of styles..."

    m 3a "But I'll always help you find what suits you the most!"

    m "So don't force yourself to write the way everyone else wants you to write."

    m "It's not like you have to worry about impressing them or anything."

    m 5 "Ahaha!"

    mc "Ahaha..."

    m 1a "Anyway, do you want to read my poem now?"

    m 1e "Don't worry, I'm not very good..."

    mc "You sound pretty confident for someone who claims to not be very good."

    m 1j "Well...that's 'cause I have to sound confident."

    m 1b "That doesn't mean I always feel that way, you know?"

    show monika 1a

    mc "I see..."

    mc "Well, let's read it, then."

    return

label ch2_m_start:

    m 1b "Hi again, [player]!"

    if n_poemearly:
        $ n_poemearly = False

        m "That was kind of silly with Natsuki earlier, wasn't it?"

        m 1j "I'm glad the two of you have been getting along so well."

        mc "..."

        "That's one way of putting it..."

        m 2a "Anyway, I already read your poem, but you can go ahead and read mine now."

        m 1a "I like the way this one turned out, so I hope you do too~"

        return
    else:
        m "How's the writing going?"

        mc "Alright, I guess..."

        m 2k "I'll take that."

        m 2b "As long as it's not going bad!"

        m 2a "I'm happy that you're applying yourself."

        m "Maybe soon you'll come up with a masterpiece!"

        mc "Ahaha, I wouldn't count on that..."

        m 2a "You never know!"

        m "Want to share what you wrote for today?"

        mc "Sure... Here you go."

        "I give my poem to Monika."

        m "..."

        m "...Alright!"

        $ nextscene = "m_" + poemwinner[1] + "_" + str(eval(poemwinner[1][0] + "_appeal"))

        call expression nextscene

        m 1a "But anyway..."

        m "You want to read my poem now?"

        m "I like the way this one turned out, so I hope you do too~"

        mc "Alright, let's take a look."

        return

label ch3_m_start:

    m 2a "Hi [player]~"

    m "Have you thought about what you want to submit to perform at the festival?"

    mc "Well..."

    "Being in this club is one thing, but performing in front of a bunch of people..."

    mc "...I'll have to give it some more thought."

    m 2b "Okay, no pressure!"

    m "But whatever you do, I'm sure it'll turn out great."

    m "It would also make me happy to see."

    m 2k "Ahaha!"

    if n_poemearly:
        $ n_poemearly = False

        m 1a "Anyway, I already read your poem, but you can go ahead and read mine now."

        return
    else:
        m 1a "Anyway, let's take a look at today's poem!"

        mc "Sure..."

        "I let Monika take the poem I'm holding in my hands."

        m "..."

        $ nextscene = "m_" + poemwinner[2] + "_" + str(eval(poemwinner[2][0] + "_appeal"))

        call expression nextscene

        m 1a "Anyway...!"

        m "I'll share my poem with you now, alright?"

        mc "Er..."

        mc "Alright..."

        return

label m_natsuki_1:
    m 2b "I like it, [player]!"

    mc "Really...?"

    m 2e "It's a lot cuter than I expected."

    m 2k "Ahahaha!"

    mc "Oh jeez..."

    m 1b "No, no!"

    m "It kind of makes me think of something Natsuki would write."

    m "And she's a good writer, too."

    m 5a "So take that as a compliment!"

    mc "Ahaha..."

    mc "If you say so."

    m "Yep!"

    m 1a "By any chance have you read anything by Shel Silverstein?"

    mc "Eh?"

    mc "Maybe a long time ago..."

    m "He's famous for telling all kinds of stories in just a few simple words."

    m "His poems can be funny, endearing, or even sad..."

    m 3d "And sometimes they're only a few lines long."

    m "They might even feel like they're written for kids, but if you think about them..."

    m "They can express views of the world that would apply to anybody."

    mc "I see..."

    mc "So you're saying that Natsuki is kind of like that?"

    m 2a "Sort of."

    m "Maybe she's not an expert..."

    m "But you probably won't find much filler in her poems."

    m "They might be easy to write, but they're super challenging to get the meaning through."

    m 2b "So I can see why it would be your kind of poem to explore!"

    return

label m_sayori_1:

    m 2a "I like this one!"

    m "It makes me think of something Sayori would like."

    mc "Is that so?"

    m 2d "You and Sayori are really good friends, right?"

    m "I wouldn't be surprised if you had those sorts of things in common."

    mc "Ah, well..."

    mc "We may be good friends, but Sayori and I are actually really different."

    m "Hmm..."

    m "Well, that may be the case."

    m 3a "But maybe there are also some similarities that you wouldn't expect."

    m "The way she talks about you..."

    m "It sounds like the two of you really care about each other's well-being."

    m "Even if you show it in different ways, it ends up being more similar than you'd think."

    m 1a "So I think that's the kind of vibe I get when reading your poem."

    mc "Hmm..."

    mc "You sure you're not reading into it too much?"

    m 5 "Ahaha! I could be!"

    m "Oh gosh, I sound like Yuri..."

    m 2a "...But in any case, Sayori's writing has kind of a gentle feel to it."

    m "I can tell that she likes exploring with emotions, like happiness and sadness."

    m "Who knew that someone so happy would enjoy sad things, too?"

    mc "Yeah... That's totally unexpected."

    m 2j "Well, to each their own~"

    m 2a "And you shouldn't be afraid to experiment a little bit, either."

    return

label m_yuri_1:

    m 1a "Great job, [player]!"

    m "I was going 'Ooh' in my head while reading it."

    m 1j "It's really metaphorical!"

    m 1a "I'm not sure why, but I didn't expect you to go for something so deep."

    m 3b "I guess I underestimated you!"

    mc "It's easiest for me to keep everyone's expectations low."

    mc "That way, it always counts when I put in some effort."

    m 5a "Ahaha! That's not very fair!"

    m "Well, I guess it worked, anyway."

    m 2a "You know that Yuri likes this kind of writing, right?"

    m "Writing that's full of imagery and symbolism."

    m 2d "Unlike Sayori, who likes using simple and direct words to describe happiness and sadness..."

    m "Yuri likes it when readers are left to derive their own meaning out of it."

    m 4d "It's very challenging to write like that effectively."

    m "Both allowing people to get something out of it just by feel..."

    m "Or letting them deeply analyze all of the nuances."

    m "It can take years of practice, which I'm assuming Yuri has at this point."

    m 1e "I never really asked, though..."

    mc "I'm sure I'm nowhere near her level yet."

    m 2b "Don't worry so much about that!"

    m "You do your own thing."

    m "Just keep exploring, and learn by trying new things!"

    return

label m_natsuki_2:

    m 1j "It's pretty good~"

    m 1a "You've been spending some time with Natsuki, haven't you?"

    m "You must like her writing style."

    mc "Ah, yeah..."

    mc "I think it's a neat way to tell a story."

    m 2a "Mhm. I don't disagree."

    m "Natsuki's poems may be cute, but they're also meaningful."

    m "I can see why you'd be into the style."

    m "I guess that means you're not as much a fan of Yuri's poems, then?"

    mc "Ah-- I wouldn't say that..."

    mc "I kind of like everyone's poems."

    m 2d "That's true, but I'm sure you like some more than others, right?"

    m "Like Yuri's use of complex words and symbolism..."

    m "Or Sayori's way of expressing happiness or sadness in a more direct way."

    m 2a "You must have some kind of preference, don't you?"

    m 4l "Ah, not that it's a contest or anything!"

    m 4a "I was just curious, that's all."

    return

label m_sayori_2:

    m 1j "It's pretty good~"

    m 1a "It makes me think of Sayori, like the other one that you wrote."

    m 4b "You two are like the dynamic duo!"

    mc "Ahaha... That's kind of exaggerating it."

    m 2a "Yeah, probably."

    m "But you do spend a lot of time with her even in this club, don't you?"

    m 2j "Then again, I don't blame you for being a little shy~"

    mc "I-I'm not shy, it's just..."

    m 5 "Ahaha! I'm just teasing."

    m "I know it takes a bit of time to make friends with everyone."

    m 2d "But Yuri and Natsuki are super interesting people, so don't be afraid to give them their share of time!"

    m "And you can talk to me every now and then too..."

    m 1e "I'm not, like, unapproachable or anything, am I?"

    mc "Ah, no, it's nothing like that..."

    mc "I'm just still getting used to being here, that's all."

    m 1a "Yeah..."

    m 1l "I'm sorry if I was putting pressure on you or something!"

    m "I really didn't mean it like that."

    mc "No, don't worry."

    mc "I get what you're saying."

    m 1a "Well, alright~"

    return

label m_yuri_2:

    m 2b "This one's good!"

    m "It feels like you're not only getting more comfortable with your style..."

    m "But the imagery is better than the last one I read!"

    m 2a "Just wondering, but have you been finding inspiration in Yuri's writing style?"

    mc "Hmm..."

    mc "I guess so."

    mc "You can't deny that she's talented."

    m 4k "Yeah, totally!"

    m 4a "I think her poems are the most..."

    m "...Romantic."

    m 1a "That's the best way to describe it."

    m 1d "She's like a totally different person when she picks up a pen..."

    mc "I noticed that, too."

    mc "Or when she's talking about literature, it's like a light turns on inside her."

    m 2a "Mhm!"

    m "Sadly, it's hard to get much personal conversation out of her..."

    m 2m "Trust me, I've tried..."

    m "Who knows what goes on in that head of hers?"

    mc "I hope you don't mean that in a bad way."

    m 1g "No, of course not!"

    m "I just meant that I wish she didn't keep so much to herself..."

    m 1e "But still, defending her like that..."

    m 5 "You must be pretty into her..."

    mc "Eh?!"

    mc "You...completely misunderstood!"

    m "Ahaha! Calm down, I'm kidding!"

    m 2a "Besides, I'm pretty sure she's already got a boyfriend..."

    mc "Wait, really?"

    m 2k "Yeah. A fictional one, anyway."

    "Monika kind of whispers that last part to me."

    m 5 "It's just a hunch, but..."

    mc "...Well, there's not really anything wrong with that!"

    m 1n "Oh, well I know...!"

    m "I was just saying~"

    return

label m_natsuki_3:

    m 2j "Sticking with the Natsuki style once more, I see~"

    m 2d "Hmm..."

    m "You really like Natsuki, don't you?"

    mc "Eh? That's--"

    m 5 "Oh, come on, [player]."

    m "It's awfully suspicious, you know?"

    m "Spending time with her in the clubroom every day..."

    m "Pretending to like the manga that she's into..."

    mc "Y-You know how Natsuki is...!"

    mc "If I don't indulge her, she'll end up hating me."

    m 2e "Eh?"

    m 2a "No, I think you're misunderstanding, [player]."

    m "It's not like Natsuki just hates anyone who doesn't give her what she wants."

    m 2d "Yeah, she's assertive, but she's not that selfish..."

    m "In fact, I think you're the only one who's indulged her as much as you have."

    mc "Is that so..."

    "I kind of knew that, but I just didn't want to admit it."

    m "So, I just need to ask one thing of you..."

    m 1e "...Be careful. Please?"

    m "Natsuki is kind of unpredictable."

    m "A lot of times, she doesn't even know what she wants."

    m 1i "After all, she's the youngest one here."

    m "She might not know how to handle her own feelings properly."

    m "What I'm saying is..."

    m 1m "If something bad happens, then it could end up damaging the club, too..."

    m 5 "And you wouldn't do that to me...right?"

    mc "That's--"

    "I'm not sure how to respond to Monika."

    "While I care about her and the club, it's also kind of unfair to bring that up."

    m "Well...you're smart."

    m "I'm sure you'll do the right thing."

    "Monika smiles sweetly."

    return

label m_sayori_3:

    m 1k "Ahaha."

    m "It's kind of funny..."

    mc "How so?"

    m 1a "No, not the poem..."

    m 2a "I mean, it's funny how your poems and Sayori's poems have been getting more and more similar to each other every day."

    m "I'm surprised you're so in sync with her."

    m 2d "Then again, you've been spending a lot of time together lately, haven't you?"

    mc "Ah, I guess you could say that..."

    mc "Although we kind of grew up as best friends, I haven't been seeing as much of her this past year..."

    mc "But since I joined the club, we've been spending a lot of time together again."

    m 1a "I see, I see~"

    m "That reminds me..."

    m "About how Sayori's been a little bit off today..."

    mc "Yeah? Did she tell you something?"

    m 1n "Ah..."

    m "Well..."

    m 2l "[player], you haven't been flirting with her, have you?"

    mc "O-Of course not!"


    mc "I've been treating her like I always do."

    m 2a "Alright."

    m 5 "Just making sure~"

    m "I know how much you care about her..."

    m "It would be terrible if something bad happened to her, so keep an eye on her."

    m 2d "Sayori's been acting so much happier ever since you joined the club."

    m "What could have happened all of a sudden...?"

    mc "..."

    m 1l "...Well, never mind."

    m "This really isn't the time to be talking about this..."

    return

label m_yuri_3:

    m 2e "Your style's gotten so refined, [player]."

    m "Yuri's been teaching you a lot of things, hasn't she?"

    mc "Well--"

    mc "I guess so."

    m 2a "Yeah... I've been noticing how much time you spend with her."

    m 2d "I think I've heard her say more words these past couple days than she's talked in the whole year."

    m "Not sure how you did it, but that's pretty impressive..."

    mc "Well, she just needs some patience and a way to talk about all the things in her head, I guess..."

    mc "I'm still getting the hang of it, myself."

    m 2a "Hm..."

    m "You're certainly putting in a lot of effort."

    m 2e "You must really like her."

    mc "Eh? That's--"

    m 5 "Ahaha!"

    m "It's awfully suspicious, you know?"

    m "Spending time with her in the clubroom every day..."

    m "Reading that edgy novel with her..."

    mc "Well--!"

    mc "I just...feel bad that she has a hard time socializing."

    mc "It makes me want to make sure she doesn't spend all her time alone."

    mc "Besides, the novel isn't too bad either, you know..."

    m 1k "Alright, alright~"

    m "I get you."

    m 1a "Just...be careful, alright?"

    m "I know that Yuri isn't used to opening herself up..."

    m 2d "So if something bad happens while she's vulnerable..."

    m "Then it could be really hard for her."

    m 2i "Her books aren't a total escape from reality."

    m "They're just a bandage."

    mc "You say that like I'm going to hurt her..."

    m 1l "Sorry, I didn't really mean that~"

    m "If anything, she might accidentally hurt herself."

    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
