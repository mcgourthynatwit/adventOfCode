package main

import (
  "fmt"
  "strings"
  "os"
  "bufio"
  "bytes"
  "strconv"
  "sort"
)

var myDict = map[string]int {
  "A": 14,
  "K": 13,
  "Q": 12,
  "J": 11,
  "T": 10,
  "9": 9,
  "8": 8,
  "7": 7,
  "6": 6,
  "5": 5,
  "4": 4,
  "3": 3,
  "2": 2,
}

var high [][5]int
var one [][5]int
var two [][5]int
var three [][5]int
var full [][5]int
var four [][5]int
var five [][5]int

var hands = make(map[[5]int]int)

// clean input to return cards and bid amount 
func clean(line string) (string, int) {
  cards, bidstr, _ := strings.Cut(line, " ")

  bid, _ := strconv.Atoi(bidstr)

  return cards, bid
}

func getAppearances(cards string) (int, int){
	pairs := make(map[string]int)

	for _, card := range cards {
		cardStr := string(card)
		pairs[cardStr]++
	}
  
  p := 0
  k := 0

  for _, value := range pairs {
    // if theres a pair and the kinds is higher then the current kinds
    if( value > 1 && value > k){
      k = value
      p ++
      continue
    }  
    // if theres a pair 
    if( value > 1 ){
      p ++
      continue 
    }   
  }
  
	return p, k
}

func getType(kind int, pairs int, cards [5]int) {
  // full house check
    if( kind == 3 && pairs == 2){
      full = append(full, cards)
      return
    } else{ 
        // check for 5, 4, 3 of a kind
	      switch(kind){
	      case 5:
	        five = append(five, cards)
	        return
	      case 4:
	        four = append(four, cards)
	        return
        case 3:
          if( pairs != 2){
            three = append(three, cards)
          } 
          return
        }
        // check if three of a kind already found to not accidently add to 2 or 1 pair
        if ( kind == 3 ){
            return
        }
        // check for pairs/high card
        switch(pairs){
          case 2:
            two = append(two, cards)
            return
          case 1:
            one = append(one,cards)
            return
          case 0:
            high = append(high, cards)
            return
        }
      }
}

// convert card strings to int for sorting
func strToInt(cards string) [5]int{
  var cardsVals [5]int 

  cardsVals[0] = myDict[string(cards[0])]
  cardsVals[1] = myDict[string(cards[1])]
  cardsVals[2] = myDict[string(cards[2])]
  cardsVals[3] = myDict[string(cards[3])]
  cardsVals[4] = myDict[string(cards[4])]

  return cardsVals
}

// sortHands sorts a slice of card value arrays
func sortHands(hands [][5]int) {
    sort.Slice(hands, func(i, j int) bool {
        for k := 0; k < 5; k++ { 
          if hands[i][k] != hands[j][k] {
                return hands[i][k] < hands[j][k]
            }
        }
        return false 
    })
}


func main(){
  fmt.Println("Hello world")

  f, _ := os.ReadFile("input.txt")
  
  reader := bytes.NewReader(f)
  scanner := bufio.NewScanner(reader)

	for scanner.Scan() {
	  cards, bid := clean(scanner.Text())
	  
	  pairs, kind := getAppearances(cards)
    cardVals := strToInt(cards)

    getType(kind, pairs, cardVals)
  
    fmt.Println("cards ", cards, "vals", cardVals)

    hands[cardVals] = bid
    }
	

	fmt.Println("high", high)
	fmt.Println("one", one)
	fmt.Println("two", two)
	fmt.Println("three", three)
	fmt.Println("full", full)
	fmt.Println("four", four)
	fmt.Println("five", five)
  
  sortHands(high)
  sortHands(one)
  sortHands(two)
  sortHands(three)
  sortHands(full)
  sortHands(four)
  sortHands(five)

  rank := 1
  total := 0
  for _, c := range(high){
    val := hands[c]
    total += val * rank
    fmt.Println("For hand ", c, " val is ", val)
    rank ++

  }
  for _, c := range(one){
    val := hands[c]
    total += val * rank
        fmt.Println("For hand ", c, " val is ", val)

    rank ++

  }
  for _, c := range(two){
      val := hands[c]
      total += val * rank
          fmt.Println("For hand ", c, " val is ", val)

      rank ++

    }
  for _, c := range(three){
      val := hands[c]
      total += val * rank
          fmt.Println("For hand ", c, " val is ", val)

      rank ++

    }
  for _, c := range(full){
      val := hands[c]
      total += val * rank
          fmt.Println("For hand ", c, " val is ", val)

      rank ++

    }
  for _, c := range(four){
      val := hands[c]
      total += val * rank
          fmt.Println("For hand ", c, " val is ", val)

      rank ++
    }
  for _, c := range(five){
      val := hands[c]
      total += val * rank
          fmt.Println("For hand ", c, " val is ", val)

      rank ++
    }
  
  fmt.Println(total, "ranl" , rank)
}
