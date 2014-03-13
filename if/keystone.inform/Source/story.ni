"keystone" by Connor McCann

A room can be scored or unscored.
The maximum score is 7.

Carry out going to a unvisited scored room:
	increment the score.

	
The Keystone is a room. "You awake on a cold stone floor to the sound of doors slamming shut. You sit up, startled. The room is small, windowless, and its only sources of light are small candles, one in each corner. The light flickers softly. As you look closer at the walls, you notice each has a shadowy recess that looks vaguely like a door. North of you is the biggest recess, it looks like stone. To the south the is the smallest recess. To the east is a shimmering door that looks to be made of some kind of metal. To the west the the door is made of wood."
After going in Keystone:
	try the player looking;
		if the player is in the Keystone for the fourth time
		begin;
			say "You see a key in the middle of the floor that you hadn't seen before…";
		end if;

The Lincoln Room is a scored room. The description is "You enter the room, and again are met with the faint glow of candle light. The floor is wooden, and there is what looks like antique furniture all around. You walk forward, and notice a dim glow out of the corner of your eye. To the West is a window, it looks like there is some kind of light source outside."

The ornate wooden door is a closed door. It is east of the Lincoln Room and west of The Keystone.

The heavy stone door is a closed door. It is north of the Keystone and south of The Instinct.

The shimmering metallic door is a closed door. It is east of the Keystone and west of the Facility.

The small door is a lockable closed door. It is locked. It is south of the Keystone and north of the Annex.

The Cathedral is a scored room. It is south of the Annex. The description is "The body of the Cathedral is imposing. The stained glass windows shoot their colored rays across the floors, and smoke rises from the candles on the alter. The smell of incense is strong. To the east is the Masoleum."

The Masoleum is a scored room. It is east of the Cathedral.
After going in Masoleum:
	try the player looking;
		if the player is in the Masoleum for the first time
		begin;
			end the game in victory;
		end if;
			

The Lincoln Window is a door. The Lincoln Window is west of The Lincoln Room and east of the Battlefield. 

Instead of searching The Lincoln Window:
	say "Through the window you make out [the other side of the window]. You think you might be able to climb through."

Instead of climbing the window:
	try entering the window.
	
Understand "climb through [something]" as climbing.
Understand "jump through [something]" as climbing.

Instead of going through the closed window:
	say "The window is shut: you'd break the glass."
		

the Battlefield is a scored room. The description is "The light you saw outside appears to be a man standing in the middle of a field with a lantern. He is too far away to see you. The moonlight illuminates the headstones that surround him. He softly whistles a song that sounds vaguely familiar."

The soldier is a man in the Battlefield. The description of the soldier is "A man in a civil-war era war uniform. He holds a lantern and sadly scans the headstones all around him."

The Instinct is a scored room. "The smell of death invades your nostrils. Frightened, you quickly scan what appears to be a cave. Straight ahead, lightning flashes and you can make out the mouth of the cave. Another flash, and you catch a glimpse of what seems to be a tiger devouring a carcass right at the entrance. You feel it shift its gaze to you. It charges straight for you and you turn to run, but the heavy stone door has shut behind you. The tiger leaps at you and you close your eyes, fearing the worst. The cave goes silent. Terrified, you open your eyes. Another flash of light, the tiger cannot be found. Another flash and crack of thunder and you can see the carcass still lies to the north at the mouth of the cave, and the blood is beginning to pool at your feet. It looks like it may be a person."

A jacket is a kind of thing. A jacket is always wearable. A pocket is a kind of container. A pocket is a part of every jacket. The carrying capacity of a pocket is always 2.

The carcass is a man in the Instinct. The description of the carcass is "The man is bloodied and crumpled. He wears a shredded blazer and bloodstained pants. You lean down to feel if he is still breathing, and to your surprise, he mutters something under his breath. You lean closer. The muttering continues, and this time you can make out what he says. '…Wa--wallet.'" The blazer is a jacket. The carcass wears the blazer. The wallet is a container. It contains an ID. The ID is a thing. The description is "Can it be? The card says your name and birthdate on it." The photograph is a thing. The description is "As you examine the photograph, lightning flashes again. It is a picture of a man with his back turned, and a large mass engulfed in flame in front of him. You feel uneasy looking at the photograph, and feel a shiver shoot down your spine." The blazer's pocket contains a wallet and a photograph.

After examining a jacket:
	let target be a random pocket which is part of the noun; say "[The target] contains [a list of things in the target]."


The facility is a scored room. The description is "The door shuts behind you and you hear a locking sound. The the room is remarkably bright, but you cannot see its source. The walls, floors, and ceiling are covered in a uniformly white, cloth-like material. In the middle of the room sits a rabbit in a cage, and next to it lies a white envelope." 

The cage is a lockable container in the facility. It is locked. It contains a rabbit. The rabbit is an animal. The description is "A white rabbit with deep black eyes. It sits, motionless, directing its lifeless gaze toward you."

The envelope is a container in the facility. The description is "A plain, white envelope. Your name is scrawled on the front in jagged, violent characters." It contains a key and a note. The key is a thing. The key unlocks the cage and the small door. The description is "The key is brass, and the eye of the key is shaped like a wing." The note is a thing. The description is "The note reads: A skull-sized kingdom awaits."
