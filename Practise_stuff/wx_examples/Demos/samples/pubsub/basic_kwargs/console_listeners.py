'''

:copyright: Copyright 2006-2009 by Oliver Schoenborn, all rights reserved.
:license: BSD, see LICENSE.txt for details.

'''

from pubsub import pub

# ------------ create some listeners --------------

class Listener:
    def onTopic11(self, msg, extra=None):
        print 'Method Listener.onTopic11 received: ', `msg`, `extra`

    def onTopic1(self, msg, topic=pub.AUTO_TOPIC):
        info = 'Method Listener.onTopic1 received "%s" message: %s'
        print info % (topic.getName(), `msg`)

    def __call__(self, **kwargs):
        print 'Listener instance received: ', kwargs

listenerObj = Listener()


def listenerFn(msg, extra=None):
    print 'Function listenerFn received: ', `msg`, `extra`

# ------------ subscribe listeners ------------------

pub.subscribe(listenerObj, pub.ALL_TOPICS) # via its __call__

pub.subscribe(listenerFn, 'topic1.subtopic11')
pub.subscribe(listenerObj.onTopic11, 'topic1.subtopic11')

pub.subscribe(listenerObj.onTopic1, 'topic1')

