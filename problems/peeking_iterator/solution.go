/*   Below is the interface for Iterator, which is already defined for you.
 *
 *   type Iterator struct {
 *       
 *   }
 *
 *   func (this *Iterator) hasNext() bool {
 *		// Returns true if the iteration has more elements.
 *   }
 *
 *   func (this *Iterator) next() int {
 *		// Returns the next element in the iteration.
 *   }
 */

type PeekingIterator struct {
    iterator *Iterator
    nextItem interface{}
}

func Constructor(iter *Iterator) *PeekingIterator {
    var peeker = &PeekingIterator{}
    peeker.iterator = iter
    peeker.nextItem = iter.next()
    return peeker
}

func (this *PeekingIterator) hasNext() bool {
    return this.nextItem != nil
}

func (this *PeekingIterator) next() int {
    var nextElem = this.nextItem
    if this.iterator.hasNext() {
        this.nextItem = this.iterator.next()
    } else {
        this.nextItem = nil
    }
    return nextElem.(int)
}

func (this *PeekingIterator) peek() int {
    return this.nextItem.(int)
}