import copy
import random


def CRC_check(messageWithNoise, P, foundError):
    # Creating a temporary copy of the message that got altered
    temp = copy.deepcopy(messageWithNoise)
    # Operating binary division between that message and the P given by the user
    index = temp.index(1) if 1 in temp else -1
    i = index
    while i < len(temp) - len(P) - 1:
        index = temp.index(1) if 1 in temp else -1
        if index != -1 and index + len(P) < len(temp):
            for j in range(len(P)):
                temp[index + j] ^= P[j]
        i += 1
    # Division remainder
    result = temp[1 - len(P):]

    # If the sum of all the array cells is 0 that means the remainder is 0
    # Remainder equal to 0 means that the message transmitted had no errors
    # Remainder not equal to 0 means that the message had errors and the CRC spotted successfully
    if sum(result) == 0:
        return foundError
    else:
        foundError += 1
        return foundError


def messageWithNoise(finalMessage, ber, errorMessage):
    # Here finalMessage is altered so we produce the altered signal based on the BER given by the user
    flag = False
    messageWithNoise = copy.deepcopy(finalMessage)
    for i in range(len(messageWithNoise)):
        # Choosing a random number between 0 and 1
        rand = random.uniform(0, 1)
        # If that number is smaller than the given BER, we alter one bit of the signal
        if rand < ber:
            flag = True
            if messageWithNoise[i] == 1:
                messageWithNoise[i] = 0
            else:
                messageWithNoise[i] = 1
    # Counting the amount of messages that got altered
    if flag:
        errorMessage += 1
    return messageWithNoise, errorMessage


def messageCreation(k, P):
    bitBlock = []
    # Creating a random sequence of k bits
    for i in range(k):
        bitBlock.append(random.randrange(0, 2))
    finalMessage = copy.deepcopy(bitBlock)

    # Adding n-k zeros in the end of the previous bit sequence
    for i in range(len(P) - 1):
        bitBlock.append(0)

    # Operating a binary division between D and P
    temp = copy.deepcopy(bitBlock)
    index = temp.index(1) if 1 in temp else -1
    i = index
    while i < len(temp) - len(P) - 1:
        index = temp.index(1) if 1 in temp else -1
        if index != -1 and index + len(P) < len(temp):
            for j in range(len(P)):
                temp[index + j] ^= P[j]
        i += 1

    # Division remainder is F
    result = temp[1 - len(P):]

    # finalMessage represents the complete signal, the T
    for i in range(len(P) - 1):
        finalMessage.append(result[i])

    return finalMessage


def main():
    errorMessages = 0
    foundError = 0
    messagesToTransmit = 100000

    print("Please enter the number of bits: ")
    k = int(input())

    print("Please enter the P message: ")
    P = [int(i) for i in str(input())]

    print("Please enter the Bit Error Rate(BER): ")
    ber = float(input())

    # Repeating the process for the desired number of messages we would like to sent
    for i in range(messagesToTransmit):
        finalMessage = messageCreation(k, P)
        alteredMessage, errorMessages = messageWithNoise(finalMessage, ber, errorMessages)
        foundError = CRC_check(alteredMessage, P, foundError)

    print("Transmitted messages: ", messagesToTransmit)
    print("Messages with errors: ", errorMessages, "out of", messagesToTransmit, "\u001b[32m(",
          (errorMessages / messagesToTransmit) * 100, "%)\u001b[0m")
    print("Messages with errors spotted by the CRC: ", foundError, "out of", errorMessages, "\u001b[32m(",
          (foundError / errorMessages) * 100, "%)\u001b[0m")
    print("Messages with errors not spotted by the CRC: ", errorMessages - foundError, "out of", errorMessages,
          "\u001b[32m(", ((errorMessages - foundError) / errorMessages) * 100, "%)\u001b[0m")



