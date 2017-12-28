# Cooper-Feeder
an application for coordinating feeding cooper everyday among roommates to avoid over feeding or under feeding.
Always waiting for button click. | create an http endpoint for the button to send a request to (/clicked)
if button clicked | when the rest request is called
record time and indicate cooper is fed | record the current time into a database indicating that cooper has been fed at this time
if button is not clicked till 9 am. start pushing notifications to feed cooper. | have a job that checks at a set time to see if cooper has been fed in the DB. If the last time fed is too long ago send notifications otherwise dont do anything
wait for email button click or actual button click for 30 min(max) | this will be unecessary
if there was a click. cooper is fed and record time | same as first case stated here
if no click after 30 min, push another notification. | same as last unecessary line
repeat till button click and a log of cooper being fed is created. | not a real case
if a notification was ever pushed out, send an update when it is logged to all other users. | needs more explicity

always waiting for button click.
if button not clicked till 7pm, start pushing notifications to feed cooper.
wait for email button click or actual button click for 30 min(max)
if there was a click. cooper is fed and record time
if no click after 30 min, push another notification.
repeat till button click and a log of cooper being fed is created.
if a notification was ever pushed out, send an update when it is logged to all other users.
