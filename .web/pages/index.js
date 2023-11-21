import { Fragment, useContext, useEffect, useRef, useState } from "react"
import { useRouter } from "next/router"
import { Event, getAllLocalStorageItems, getRefValue, getRefValues, isTrue, preventDefault, refs, spreadArraysOrObjects, uploadFiles, useEventLoop } from "/utils/state"
import { ColorModeContext, EventLoopContext, initialEvents, StateContext } from "/utils/context.js"
import "focus-visible/dist/focus-visible"
import { Box, Center, Divider, Grid, GridItem, Heading, HStack, Image, Link, Modal, ModalBody, ModalContent, ModalHeader, ModalOverlay, Text, Tooltip, VStack } from "@chakra-ui/react"
import { getEventURL } from "/utils/state.js"
import NextLink from "next/link"
import { ExternalLinkIcon } from "@chakra-ui/icons"
import NextHead from "next/head"



export default function Component() {
  const state = useContext(StateContext)
  const router = useRouter()
  const [ colorMode, toggleColorMode ] = useContext(ColorModeContext)
  const focusRef = useRef();
  
  // Main event loop.
  const [addEvents, connectError] = useContext(EventLoopContext)

  // Set focus to the specified element.
  useEffect(() => {
    if (focusRef.current) {
      focusRef.current.focus();
    }
  })

  // Route after the initial page hydration.
  useEffect(() => {
    const change_complete = () => addEvents(initialEvents())
    router.events.on('routeChangeComplete', change_complete)
    return () => {
      router.events.off('routeChangeComplete', change_complete)
    }
  }, [router])

  const ref_footer = useRef(null); refs['ref_footer'] = ref_footer;
  const ref_portafolio = useRef(null); refs['ref_portafolio'] = ref_portafolio;

  return (
    <Fragment>
  <Fragment>
  {isTrue(connectError !== null) ? (
  <Fragment>
  <Modal isOpen={connectError !== null}>
  <ModalOverlay>
  <ModalContent>
  <ModalHeader>
  {`Connection Error`}
</ModalHeader>
  <ModalBody>
  <Text>
  {`Cannot connect to server: `}
  {(connectError !== null) ? connectError.message : ''}
  {`. Check if server is reachable at `}
  {getEventURL().href}
</Text>
</ModalBody>
</ModalContent>
</ModalOverlay>
</Modal>
</Fragment>
) : (
  <Fragment/>
)}
</Fragment>
  <Box>
  <Box sx={{"width": "100%", "display": ["none", "none", "none", "block"]}}>
  <HStack justify={`space-between`} sx={{"position": "sticky", "paddingX": "8em", "paddingY": "1em", "top": "0", "bg": "#05192d", "zIndex": "999", "id": "home", "backdropFilter": "blur(10px)", "_webkitBackdropFilter": "blur(10px)"}}>
  <Link as={NextLink} href={``} sx={{"_hover": {"color": "#60e6ff"}}}>
  <HStack>
  <Image src={`lupy.png`} sx={{"height": "3em", "width": "100%"}}/>
  <Heading sx={{"fontSize": "1.5em", "color": "#60e6ff"}}>
  {`Lupy`}
</Heading>
</HStack>
</Link>
  <HStack>
  <Link as={NextLink} href={`#portafolio`} sx={{"borderRight": "0.2em solid #05bdfb", "marginLeft": "0px !important", "paddingX": "0.5em", "_hover": {"color": "#60e6ff"}}}>
  {`Portafolio`}
</Link>
  <Link as={NextLink} href={`#experiencia`} sx={{"borderRight": "0.2em solid #05bdfb", "marginLeft": "0px !important", "paddingX": "0.5em", "_hover": {"color": "#60e6ff"}}}>
  {`Experiencia`}
</Link>
  <Link as={NextLink} href={`#contacto`} sx={{"marginLeft": "0px !important", "paddingX": "0.5em", "_hover": {"color": "#60e6ff"}}}>
  {`Contacto`}
</Link>
</HStack>
</HStack>
  <Center sx={{"marginTop": "8em"}}>
  <VStack sx={{"gap": "3em"}}>
  <HStack sx={{"gap": "2em"}}>
  <Box sx={{"position": "relative", "height": "19em", "width": "19em", "borderRadius": "0.5em", "bg": "#7833fe"}}>
  <Image alt={`Profile picture`} src={`https://i.postimg.cc/VkHYXNX7/profile.png`} sx={{"border": "0.2em solid #05bdfb", "position": "absolute", "marginLeft": "1em", "marginTop": "1em", "borderRadius": "0.5em", "bg": "#213147", "zIndex": "10", "width": "100%", "height": "100%"}}/>
</Box>
  <VStack alignItems={`start`} sx={{"width": "19em", "gap": "0.5em"}}>
  <Heading sx={{"fontSize": "2em", "color": "#FFFFF2"}}>
  {`Backend Developer`}
</Heading>
  <Text sx={{"fontSize": "1.5em", "fontWeight": "bold"}}>
  {`Luis Guzmán`}
</Text>
  <Text sx={{"fontWeight": "bold", "color": "#60e6ff"}}>
  {`@lupydev`}
</Text>
  <HStack sx={{"marginTop": "0.5em"}}>
  <Tooltip label={`GitHub`}>
  <Link as={NextLink} href={`https://github.com/lupydev`} isExternal={true} sx={{"padding": "0.5em", "borderRadius": "0.5em", "bg": "#7833fe", "_hover": {"bg": "#974cff"}, "justifyItem": "center"}}>
  <Image src={`icons/github.svg`} sx={{"height": "2em", "width": "100%"}}/>
</Link>
</Tooltip>
  <Tooltip label={`LinkedIn`}>
  <Link as={NextLink} href={`https://www.linkedin.com/in/lupydev/`} isExternal={true} sx={{"padding": "0.5em", "borderRadius": "0.5em", "bg": "#7833fe", "_hover": {"bg": "#974cff"}, "justifyItem": "center"}}>
  <Image src={`icons/linkedin.svg`} sx={{"height": "2em", "width": "100%"}}/>
</Link>
</Tooltip>
  <Tooltip label={`Curriculum Vitae`}>
  <Link as={NextLink} href={``} isExternal={true} sx={{"padding": "0.5em", "borderRadius": "0.5em", "bg": "#7833fe", "_hover": {"bg": "#974cff"}, "justifyItem": "center"}}>
  <Image src={`icons/floppy.svg`} sx={{"height": "2em", "width": "100%"}}/>
</Link>
</Tooltip>
</HStack>
</VStack>
</HStack>
  <Text sx={{"maxWidth": "40em"}}>
  {`Soy un desarrollador python con un año de experiencia. Mi objetivo principal es aprender y crecer constantemente mientras contribuyo al mundo de la tecnología. Durante mi tiempo de aprendizaje he estado enfocándome en adquirir sólidos conocimientos en Django REST framework y FastAPI para desarrollar RESTful APIs de calidad. Estoy emocionado por las oportunidades que estas tecnologías brindan para crear aplicaciones o páginas webs de alto rendimiento y escalabilidad.`}
</Text>
</VStack>
</Center>
  <Center id={`portafolio`} ref={ref_portafolio} sx={{"paddingTop": "8em"}}>
  <VStack alignItems={`start`} sx={{"borderRadius": "0.5em"}}>
  <Heading sx={{"fontSize": "2em", "color": "#FFFFF2", "alignSelf": "start", "marginBottom": "0.5em"}}>
  {`Portafolio`}
</Heading>
  <VStack sx={{"gap": "2em"}}>
  <Box sx={{"position": "relative", "width": "41em", "height": "20em", "margin": "0px !important", "borderRadius": "0.5em", "bg": "#7833fe"}}>
  <Grid sx={{"border": "0.2em solid #05bdfb", "width": "100%", "height": "100%", "borderRadius": "0.5em", "marginTop": "1em", "marginLeft": "1em", "position": "absolute", "zIndex": "10", "bg": "#213147"}} templateColumns={`repeat(2, 1fr)`}>
  <GridItem sx={{"position": "relative", "padding": "0.8em"}}>
  <VStack alignItems={`start`}>
  <Heading sx={{"fontSize": "1.5em", "color": "#FFFFF2"}}>
  {`El Buen Conejo`}
</Heading>
  <Divider sx={{"borderColor": "#60e6ff"}}/>
  <VStack>
  <Text>
  {`Plataforma web que reune al gremio de cunicultores para impulsar el sector, las granjas de criaderos y el consumo de carne de conejo como alternativa a otras proteinas animales, además de dar visibilidad a los productores y crear comunidad.`}
</Text>
  <HStack sx={{"position": "absolute", "bottom": "0.8em", "right": "0.8em"}}>
  <Link as={NextLink} href={`https://el-buen-conejo-p77dvghrt-jaardila-3.vercel.app/`} isExternal={true} sx={{"padding": "0.5em", "borderRadius": "0.5em", "bg": "#7833fe", "_hover": {"bg": "#974cff"}, "justifyItem": "center"}}>
  <Image src={`icons/external_link.svg`} sx={{"height": "1em", "width": "100%"}}/>
</Link>
  <Link as={NextLink} href={`https://github.com/lupydev/el-buen-conejo`} isExternal={true} sx={{"padding": "0.5em", "borderRadius": "0.5em", "bg": "#7833fe", "_hover": {"bg": "#974cff"}, "justifyItem": "center"}}>
  <Image src={`icons/github.svg`} sx={{"height": "1em", "width": "100%"}}/>
</Link>
</HStack>
</VStack>
</VStack>
</GridItem>
  <GridItem>
  <Image alt={`conejon`} src={`https://res.cloudinary.com/dzc8agefr/image/upload/v1699939914/1_vdi3km.png`} sx={{"opacity": "0.7", "bg": "#7833fe", "borderTopRightRadius": "0.5em", "borderBottomRightRadius": "0.5em", "width": "100%", "height": "100%"}}/>
</GridItem>
</Grid>
</Box>
  <Box sx={{"position": "relative", "width": "41em", "height": "20em", "margin": "0px !important", "borderRadius": "0.5em", "bg": "#7833fe"}}>
  <Grid sx={{"border": "0.2em solid #05bdfb", "width": "100%", "height": "100%", "borderRadius": "0.5em", "marginTop": "1em", "marginLeft": "1em", "position": "absolute", "zIndex": "10", "bg": "#213147"}} templateColumns={`repeat(2, 1fr)`}>
  <GridItem sx={{"position": "relative", "padding": "0.8em"}}>
  <VStack alignItems={`start`}>
  <Heading sx={{"fontSize": "1.5em", "color": "#FFFFF2"}}>
  {`El Buen Conejo`}
</Heading>
  <Divider sx={{"borderColor": "#60e6ff"}}/>
  <VStack>
  <Text>
  {`Plataforma web que reune al gremio de cunicultores para impulsar el sector, las granjas de criaderos y el consumo de carne de conejo como alternativa a otras proteinas animales, además de dar visibilidad a los productores y crear comunidad.`}
</Text>
  <HStack sx={{"position": "absolute", "bottom": "0.8em", "right": "0.8em"}}>
  <Link as={NextLink} href={`https://el-buen-conejo-p77dvghrt-jaardila-3.vercel.app/`} isExternal={true} sx={{"padding": "0.5em", "borderRadius": "0.5em", "bg": "#7833fe", "_hover": {"bg": "#974cff"}, "justifyItem": "center"}}>
  <Image src={`icons/external_link.svg`} sx={{"height": "1em", "width": "100%"}}/>
</Link>
  <Link as={NextLink} href={`https://github.com/lupydev/el-buen-conejo`} isExternal={true} sx={{"padding": "0.5em", "borderRadius": "0.5em", "bg": "#7833fe", "_hover": {"bg": "#974cff"}, "justifyItem": "center"}}>
  <Image src={`icons/github.svg`} sx={{"height": "1em", "width": "100%"}}/>
</Link>
</HStack>
</VStack>
</VStack>
</GridItem>
  <GridItem>
  <Image alt={`conejon`} src={`https://res.cloudinary.com/dzc8agefr/image/upload/v1699939914/1_vdi3km.png`} sx={{"opacity": "0.7", "bg": "#7833fe", "borderTopRightRadius": "0.5em", "borderBottomRightRadius": "0.5em", "width": "100%", "height": "100%"}}/>
</GridItem>
</Grid>
</Box>
  <Box sx={{"position": "relative", "width": "41em", "height": "20em", "margin": "0px !important", "borderRadius": "0.5em", "bg": "#7833fe"}}>
  <Grid sx={{"border": "0.2em solid #05bdfb", "width": "100%", "height": "100%", "borderRadius": "0.5em", "marginTop": "1em", "marginLeft": "1em", "position": "absolute", "zIndex": "10", "bg": "#213147"}} templateColumns={`repeat(2, 1fr)`}>
  <GridItem sx={{"position": "relative", "padding": "0.8em"}}>
  <VStack alignItems={`start`}>
  <Heading sx={{"fontSize": "1.5em", "color": "#FFFFF2"}}>
  {`El Buen Conejo`}
</Heading>
  <Divider sx={{"borderColor": "#60e6ff"}}/>
  <VStack>
  <Text>
  {`Plataforma web que reune al gremio de cunicultores para impulsar el sector, las granjas de criaderos y el consumo de carne de conejo como alternativa a otras proteinas animales, además de dar visibilidad a los productores y crear comunidad.`}
</Text>
  <HStack sx={{"position": "absolute", "bottom": "0.8em", "right": "0.8em"}}>
  <Link as={NextLink} href={`https://el-buen-conejo-p77dvghrt-jaardila-3.vercel.app/`} isExternal={true} sx={{"padding": "0.5em", "borderRadius": "0.5em", "bg": "#7833fe", "_hover": {"bg": "#974cff"}, "justifyItem": "center"}}>
  <Image src={`icons/external_link.svg`} sx={{"height": "1em", "width": "100%"}}/>
</Link>
  <Link as={NextLink} href={`https://github.com/lupydev/el-buen-conejo`} isExternal={true} sx={{"padding": "0.5em", "borderRadius": "0.5em", "bg": "#7833fe", "_hover": {"bg": "#974cff"}, "justifyItem": "center"}}>
  <Image src={`icons/github.svg`} sx={{"height": "1em", "width": "100%"}}/>
</Link>
</HStack>
</VStack>
</VStack>
</GridItem>
  <GridItem>
  <Image alt={`conejon`} src={`https://res.cloudinary.com/dzc8agefr/image/upload/v1699939914/1_vdi3km.png`} sx={{"opacity": "0.7", "bg": "#7833fe", "borderTopRightRadius": "0.5em", "borderBottomRightRadius": "0.5em", "width": "100%", "height": "100%"}}/>
</GridItem>
</Grid>
</Box>
</VStack>
</VStack>
</Center>
  <VStack id={`footer`} ref={ref_footer} sx={{"marginTop": "4em", "marginBottom": "1em", "width": "100%"}}>
  <Text sx={{"marginY": "0px !important"}}>
  {`Esta web fue creada en `}
  <Text as={`span`} sx={{"fontWeight": "bold", "color": "#05bdfb"}}>
  {`Python puro `}
</Text>
  {`con el framework: `}
  <Link as={NextLink} href={`https://reflex.dev/`} sx={{"fontWeight": "bold", "color": "#05bdfb", "textDecoration": "underline", "_hover": {"color": "#60e6ff"}}}>
  {`Reflex`}
  <ExternalLinkIcon/>
</Link>
</Text>
  <Text sx={{"marginY": "0px !important"}}>
  {`© 2023 hecho con `}
  <Text as={`span`} sx={{"color": "#7833fe"}}>
  {`❤`}
</Text>
  {` por: `}
  <Text as={`span`} sx={{"fontWeight": "bold", "color": "#05bdfb"}}>
  {`Lupy, `}
</Text>
  <Text as={`span`}>
  {`de Colombia para el 🌎`}
</Text>
</Text>
</VStack>
</Box>
</Box>
  <NextHead>
  <title>
  {`Lupy | Backend Developer`}
</title>
  <meta content={`Hola, mi nombre es Luis Guzmán. Soy Desarrollador Backend y Python Developer`} name={`description`}/>
  <meta content={`favicon.ico`} property={`og:image`}/>
</NextHead>
</Fragment>
  )
}
