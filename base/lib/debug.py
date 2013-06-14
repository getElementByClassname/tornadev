import logging
import tornado.escape
import tornado.websocket


class Debug(tornado.websocket.WebSocketHandler):
  waiters = set()

  def allow_draft76(self):
    # for iOS 5.0 Safari
    return True

  def open(self):
    print 'connected'
    Debug.waiters.add(self)

  def on_close(self):
    Debug.waiters.remove(self)

  @classmethod
  def emit(cls, chat):
    logging.info("sending message to %d waiters", len(cls.waiters))
    for waiter in cls.waiters:
      try:
        waiter.write_message(chat)
      except:
        logging.error("Error sending message", exc_info=True)

  def on_message(self, message):
    Debug.emit(message)
