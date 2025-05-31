You're working on updating the cropping in the isolate_score function.

There's also some weird bug where sometimes running both `get_screen` and 
`isolate_score` does not result in the existence of two screenshots. Or maybe 
that's just Cursor not picking up filesystem changes.