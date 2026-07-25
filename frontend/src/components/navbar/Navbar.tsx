function Navbar() {
  return (
    <header className="h-16 border-b flex items-center justify-between px-6">

      <h2 className="text-lg font-semibold">
        Dashboard
      </h2>


      <div className="flex items-center gap-3">

        <span className="text-sm text-gray-500">
          Device
        </span>

        <span className="bg-green-100 text-green-700 px-3 py-1 rounded-full text-sm">
          Online
        </span>

      </div>

    </header>
  )
}

export default Navbar