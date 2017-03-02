from IPython.core.completer import IPCompleter

class RLCompleter(IPCompleter):


    def rlcomplete(self, text, state):
        """Return the state-th possible completion for 'text'.
        This is called successively with state == 0, 1, 2, ... until it
        returns None.  The completion should begin with 'text'.
        Parameters
        ----------
          text : string
            Text to perform the completion on.
          state : int
            Counter used by readline.
        """
        #from there import print

        if state==0:

            self.line_buffer = line_buffer = self.readline.get_line_buffer()
            cursor_pos = self.readline.get_endidx()

            #io.rprint("\nRLCOMPLETE: %r %r %r" %
            #          (text, line_buffer, cursor_pos) ) # dbg

            # if there is only a tab on a line with only whitespace, instead of
            # the mostly useless 'do you want to see all million completions'
            # message, just do the right thing and give the user his tab!
            # Incidentally, this enables pasting of tabbed text from an editor
            # (as long as autoindent is off).

            # It should be noted that at least pyreadline still shows file
            # completions - is there a way around it?

            # don't apply this on 'dumb' terminals, such as emacs buffers, so
            # we don't interfere with their own tab-completion mechanism.
            if not (self.dumb_terminal or line_buffer.strip()):
                self.readline.insert_text('\t')
                sys.stdout.flush()
                return None

            # Note: debugging exceptions that may occur in completion is very
            # tricky, because readline unconditionally silences them.  So if
            # during development you suspect a bug in the completion code, turn
            # this flag on temporarily by uncommenting the second form (don't
            # flip the value in the first line, as the '# dbg' marker can be
            # automatically detected and is used elsewhere).
            DEBUG = False
            #DEBUG = True # dbg
            if DEBUG:
                try:
                    self.complete(text, line_buffer, cursor_pos)
                except:
                    import traceback; traceback.print_exc()
            else:
                # The normal production version is here

                # This method computes the self.matches array
                self.complete(text, line_buffer, cursor_pos)
        try:
            return self.matches[state]
        except IndexError:
            return None

