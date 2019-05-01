import random
import pprint
import math

DEFAULT_NUM_THANOSES = 63
DEFAULT_NUM_PEOPLE = 7_500_000_000

class Thanos(object):

	def __init__( self ):
		self.dead = False
		self.snapped = False

	def Snap( self, currentPopulation, thanosList ):
		self.snapped = True

		for thanos in thanosList:
			if( not thanos.dead ):
				thanos.dead = ( random.random() > 0.5 )

		return int(currentPopulation / 2)

	@staticmethod
	def RunThanosSim( numThanoses = DEFAULT_NUM_THANOSES, numPeople = DEFAULT_NUM_PEOPLE ):
		thanosList = []

		for i in range( numThanoses ):
			thanosList.append( Thanos() )

		snappingCtr = 0
		currentPopulation = numPeople

		while( snappingCtr < numThanoses ):
			currentPopulation = thanosList[ snappingCtr ].Snap( currentPopulation, thanosList )

			snappingCtr += 1
			while( snappingCtr < numThanoses ):
				
				if( thanosList[ snappingCtr ].dead ):
					snappingCtr += 1
				else:
					break

		return currentPopulation

	@staticmethod
	def RunManySims( numTimesToRun, numThanoses = DEFAULT_NUM_THANOSES, numPeople = DEFAULT_NUM_PEOPLE ):

		populationToCountMap = {}

		for i in range( numTimesToRun ):
			thisPopulation = Thanos.RunThanosSim( numThanoses, numPeople )

			if thisPopulation not in populationToCountMap:
				populationToCountMap[ thisPopulation ] = 1
			else:
				populationToCountMap[ thisPopulation ] += 1

		pprint.pprint( populationToCountMap )

		weightedAvg = 0
		for thisPopulation in populationToCountMap:
			weightedAvg += ( thisPopulation ) * ( populationToCountMap[ thisPopulation ] / numTimesToRun )
		
		return int( weightedAvg )

def main():
	weightedAvg = Thanos.RunManySims( 50_000 )
	print( "Weighted average: {:,}".format( weightedAvg ) )

if __name__ == '__main__':
	main()